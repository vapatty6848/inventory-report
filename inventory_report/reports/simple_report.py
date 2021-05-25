from datetime import date


class SimpleReport:
  @classmethod
    def generate(class, inventory):
      date_today = str(date.today())

      oldest_item = min([item["data_de_fabricacao"] for item in inventory])