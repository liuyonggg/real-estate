class Analyzer(object):
    def analyze(self, filename, cities_file):
        f = open(filename, "r")
        data = f.read().split(",")
        f.close()

        f = open(cities_file, "r")
        cities = set()
        cities_data = f.read().split(',')
        for city in cities_data:
            cities.add(city)
        f.close()

        f = open("output.csv", "w")
        prices = []
        record = False
        res = {}
        city = ""
        for i in range(len(data)):
            if data[i] == "City":
                if int(data[i-2]) > 2400:
                    break
                elif data[i-1] in cities:
                    city = data[i-1]
                    record = True
            elif record:
                try:
                    price = float(data[i])
                    if "." not in data[i]:
                        res[city] = (prices[-1] - prices[0]) / prices[0] * 100
                        prices = []
                        record = False
                    else:
                        prices.append(float(data[i]))
                        if len(prices) > 121:
                            prices.pop(0)

                except:
                    continue

        for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True):
            f.write(k + "," + str(v) + "\n")

        f.close()


    def analyzeUS(self, filename):
        f = open(filename, "r")
        data = f.read().split(",")
        f.close()

        f = open("output.csv", "w")
        prices = []
        record = False
        res = {}
        city = ""
        for i in range(len(data)):
            if data[i] == "City":
                if int(data[i-2]) > 2400:
                    break
                city = data[i-1]
                record = True
            elif record:
                try:
                    price = float(data[i])
                    if "." not in data[i]:
                        res[city] = (prices[-1] - prices[0]) / prices[0] * 100
                        prices = []
                        record = False
                    else:
                        prices.append(float(data[i]))
                        if len(prices) > 121:
                            prices.pop(0)

                except:
                    continue

        for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True):
            f.write(k + "," + str(v) + "\n")

        f.close()


if __name__ == "__main__":
    a = Analyzer()
    print(a.analyze("Real_Estate_data.csv", "Cities.csv"))
