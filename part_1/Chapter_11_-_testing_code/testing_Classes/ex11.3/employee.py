class Employee:
    """Отличный работяга. Самый лучший."""

    def __init__(self, name, surname, salary):
        """Инициализирует аргументы."""
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, delta=5000):
        """Повышение зарплаты на заданную величину delta.
        По умолчанию величина = 5000."""
        self.salary = self.salary + delta
        return self.salary