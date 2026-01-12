
from TFLGreenhouse.Climate import Climate
class Farm:
    def __init__(self, rows, columns):
        self.rows =  rows
        self.columns = columns
        self.greenhouse = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                greenHouse = Climate()
                row.append(greenHouse)
            self.greenhouse.append(row)

    def display(self):
        for row in range(self.rows):
            for column in range(self.columns):
                theGreenhouse = self.greenhouse[row][column]
                print(
                    f"[R{row+1}C{column+1}] "
                    f"T={theGreenhouse.temperature:.1f}°C "
                    f"H={theGreenhouse.humidity:.1f}% "
                    f"L={int(theGreenhouse.lightIntensity)} Lux "
                    f"CO₂={theGreenhouse.co2:.0f}ppm "
                    f"SM={theGreenhouse.soilMoisture:.1f}%",
                    end="\t"
                )
            print()