#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, topic: str, data: str) -> None:
        pass


class LogObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


class NewsSubject:
    def __init__(self) -> None:
        self._subscribers: dict[Observer, set[str] | None] = {}

    def subscribe(self, observer: Observer, topics: set[str] | None = None) -> None:
        self._subscribers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        self._subscribers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        for observer, topics in list(self._subscribers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


def main() -> None:
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer, topics=None)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
