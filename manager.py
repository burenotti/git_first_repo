from worker import Worker

class Manager(Worker):
	def __init__(self, hour_pay, hour_bonus):
		super().__init__(hour_pay)
		self._hour_pay = hour_pay
		self._hour_bonus = hour_bonus

	def get_total_bonus(self, days):
		return days * (1+self._hour_bonus) * self._hour_pay

	def get_total_pay(self, days):
		return Worker.get_total_pay(days) + self.get_total_bonus(days)
