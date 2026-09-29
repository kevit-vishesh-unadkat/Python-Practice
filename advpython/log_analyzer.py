
import re
from collections import Counter


LOG_FILE = "mysterybox.log"


# ============================================================
# 1. REGEX PATTERNS
# ============================================================

# Valid log line
VALID_LOG_PATTERN = re.compile(
    r"^\s*"
    r"(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})"
    r"\s*\|\s*"
    r"(?P<level>INFO|WARNING|ERROR)"
    r"\s*\|\s*"
    r"(?P<fields>.+)"
    r"\s*$"
)


# Individual key=value field
FIELD_PATTERN = re.compile(
    r"(?P<key>[A-Za-z_][A-Za-z0-9_]*)="
    r"(?P<value>[^|]+)"
)


# Card number: exactly 16 digits
CARD_PATTERN = re.compile(r"\b\d{16}\b")


# Suspicious download:
# filename must contain:
#   secret OR backup OR admin OR password
# AND end with:
#   .zip OR .exe OR .sh
SUSPICIOUS_DOWNLOAD_PATTERN = re.compile(
    r"file=[^|]*(?:secret|backup|admin|password)[^|]*"
    r"\.(?:zip|exe|sh)\b",
    re.IGNORECASE
)


# Suspicious login using positive lookaheads.
#
# The line must contain:
#   WARNING or ERROR
#   user=...
#   action=login_failed
SUSPICIOUS_LOGIN_PATTERN = re.compile(
    r"^(?=.*\|\s*(?:WARNING|ERROR)\s*\|)"
    r"(?=.*\|\s*user=[^|]+)"
    r"(?=.*\|\s*action=login_failed\b).*$"
)


# Extract user from a login_failed record
USER_PATTERN = re.compile(
    r"\|\s*user=(?P<user>[^|]+)"
)


# ============================================================
# 2. ANALYZER
# ============================================================

def analyze_log(filename):
    total_lines = 0
    valid_lines = 0
    invalid_lines = 0

    level_counts = Counter()
    users = set()

    suspicious_login_count = 0
    failed_login_users = Counter()

    suspicious_download_count = 0
    card_numbers_masked = 0

    parsed_records = []

    with open(filename, "r", encoding="utf-8") as file:

        for raw_line in file:

            total_lines += 1
            line = raw_line.strip()

            # ------------------------------------------------
            # Validate log line
            # ------------------------------------------------
            match = VALID_LOG_PATTERN.fullmatch(line)

            if not match:
                invalid_lines += 1
                continue

            valid_lines += 1

            timestamp = match.group("timestamp")
            level = match.group("level")
            fields_text = match.group("fields")

            # ------------------------------------------------
            # Extract key=value fields
            # ------------------------------------------------
            fields = {}

            for field_match in FIELD_PATTERN.finditer(fields_text):

                key = field_match.group("key")
                value = field_match.group("value").strip()

                fields[key] = value

            # ------------------------------------------------
            # Make sure there is at least one valid key=value
            # field.
            # ------------------------------------------------
            if not fields:
                # Technically this line matched the outer
                # structure but contains no key=value fields.
                valid_lines -= 1
                invalid_lines += 1
                continue

            record = {
                "timestamp": timestamp,
                "level": level,
                "fields": fields
            }

            parsed_records.append(record)

            # ------------------------------------------------
            # Count log levels
            # ------------------------------------------------
            level_counts[level] += 1

            # ------------------------------------------------
            # Count unique users
            # ------------------------------------------------
            if "user" in fields:
                users.add(fields["user"])

            # ------------------------------------------------
            # Suspicious login detection
            # ------------------------------------------------
            if SUSPICIOUS_LOGIN_PATTERN.search(line):

                suspicious_login_count += 1

                user_match = USER_PATTERN.search(line)

                if user_match:
                    user = user_match.group("user").strip()
                    failed_login_users[user] += 1

            # ------------------------------------------------
            # Suspicious downloads
            # ------------------------------------------------
            if (
                fields.get("action") == "download"
                and SUSPICIOUS_DOWNLOAD_PATTERN.search(line)
            ):
                suspicious_download_count += 1

            # ------------------------------------------------
            # Mask card numbers
            # ------------------------------------------------
            masked_line, count = CARD_PATTERN.subn(
                "****MASKED****",
                line
            )

            card_numbers_masked += count

    # Users with at least 2 failed logins
    repeated_failed_users = {
        user: count
        for user, count in failed_login_users.items()
        if count >= 2
    }

    return {
        "total_lines": total_lines,
        "valid_lines": valid_lines,
        "invalid_lines": invalid_lines,
        "level_counts": level_counts,
        "unique_users": users,
        "suspicious_login_count": suspicious_login_count,
        "failed_login_users": failed_login_users,
        "repeated_failed_users": repeated_failed_users,
        "suspicious_download_count": suspicious_download_count,
        "card_numbers_masked": card_numbers_masked,
        "records": parsed_records
    }


# ============================================================
# 3. REPORT
# ============================================================

def print_report(result):

    print("\n" + "=" * 50)
    print("        MYSTERYBOX LOG ANALYZER")
    print("=" * 50)

    print(f"Total lines              : {result['total_lines']}")
    print(f"Valid lines              : {result['valid_lines']}")
    print(f"Invalid lines            : {result['invalid_lines']}")

    print("\n--- Log Levels ---")
    print(f"INFO                     : {result['level_counts']['INFO']}")
    print(f"WARNING                  : {result['level_counts']['WARNING']}")
    print(f"ERROR                    : {result['level_counts']['ERROR']}")

    print("\n--- User Activity ---")
    print(f"Unique application users : {len(result['unique_users'])}")

    print("\n--- Suspicious Activity ---")
    print(
        f"Suspicious login records : "
        f"{result['suspicious_login_count']}"
    )

    print(
        f"Suspicious downloads     : "
        f"{result['suspicious_download_count']}"
    )

    print("\n--- Failed Login Users ---")

    if result["repeated_failed_users"]:
        for user, count in result["repeated_failed_users"].items():
            print(f"{user}: {count} failed attempts")
    else:
        print("None")

    print("\n--- Sensitive Data ---")
    print(
        f"Card numbers masked      : "
        f"{result['card_numbers_masked']}"
    )

    print("=" * 50)


# ============================================================
# 4. MAIN
# ============================================================

def main():

    try:
        result = analyze_log(LOG_FILE)
        print_report(result)

    except FileNotFoundError:
        print(f"Error: '{LOG_FILE}' was not found.")


if __name__ == "__main__":
    main()
