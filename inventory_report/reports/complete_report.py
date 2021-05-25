from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, stock):
        report = super().generate(stock)

        name_list = []
        for item in stock:
            name_list.append(item["nome_da_empresa"])

        repeat_name = []
        quantity_list = []
        for name in name_list:
            if name not in repeat_name:
                quantity_list.append(name_list.count(name))
                repeat_name.append(name)

        second_report = ""

        for x in range(0, len(repeat_name)):
            second_report += f"- {repeat_name[x]}: {quantity_list[x]}\n"

        return (
            report
            + "\n"
            + "Produtos estocados por empresa: \n"
            + second_report
        )
