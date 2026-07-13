from mailwatch.core.parser import parse_email


def test_parse_email():
    raw = b"""\
Subject: Hello
From: sender@example.com
To: test@example.com

MailWatch body
"""

    result = parse_email(raw)

    assert result["subject"] == "Hello"
    assert result["body"] == "MailWatch body"