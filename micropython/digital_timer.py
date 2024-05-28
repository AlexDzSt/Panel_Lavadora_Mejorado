class DigitalTimer:
    def __init__(self, m: int = 0, s: int = 0) -> None:
        """Constructs a digital timer object from two parameters (m, s)

        Args:
            m (int, optional): The current minutes. Defaults to 0.
            s (int, optional): The current seconds. Defaults to 0.
        """
        assert m < 60 and m >= 0
        self.__m = m
        assert s < 60 and s >= 0
        self.__s = s

    def get_time(self) -> "tuple[int, int]":
        """Returns the current time the digital clock holds

        Returns:
            tuple[int, int]: m, s
        """
        return self.__m, self.__s

    def clear_time(self) -> None:
        """Clear the current time
        """
        self.__m, self.__s = 0, 0

    def decrement(self) -> None:
        """Decrement one second the current time
        """
        if self.__s == 0:
            self.__m = self.__m - 1 if self.__m > 0 else 59
        self.__s = self.__s - 1 if self.__s > 0 else 59