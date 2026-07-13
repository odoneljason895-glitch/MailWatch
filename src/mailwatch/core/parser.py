from email import message_from_bytes


def parse_email(raw_bytes):
    msg = message_from_bytes(raw_bytes)

    subject = msg.get("Subject", "")
    sender = msg.get("From", "")
    recipient = msg.get("To", "")

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(
                    decode=True
                )

                if payload:
                    body = payload.decode(
                        errors="ignore"
                    )
                    break
    else:
        payload = msg.get_payload(
            decode=True
        )

        if payload:
            body = payload.decode(
                errors="ignore"
            )

    return {
        "subject": subject,
        "sender": sender,
        "recipient": recipient,
        "body": body.strip(),
    }