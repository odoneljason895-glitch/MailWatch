from mailwatch.core.app import MailWatchApp


def main():
    app = MailWatchApp(
        "src/mailwatch/config/accounts.yml",
        "src/mailwatch/config/rules.yml",
    )

    app.start()

    print("MailWatch running")
    print(app.status())

    results = app.scheduler.run_once()

    print("Scheduler result:")
    print(results)


if __name__ == "__main__":
    main()