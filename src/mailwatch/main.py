from mailwatch.core.app import MailWatchApp


def main():
    app = MailWatchApp(
        "src/mailwatch/config/accounts.yml",
        "src/mailwatch/config/rules.yml",
    )

    app.start()

    print("MailWatch started")
    print(app.status())

    for result in app.poll():
        print(result)


if __name__ == "__main__":
    main()