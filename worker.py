class Worker:
	def __init__(self, hour_pay):
		self._hour_pay = hour_pay

	def get_pay(self, days):
		return self._hour_pay * 8 * days

	def get_total_pay(self, days, tax=.13):
		return self.get_pay(days) * 1-tax

