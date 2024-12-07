from pprint import pprint #為了看dict好看一點
import tools

def main():
    sitenames:list[str] = tools.get_sitenames('aqi.xlsx')
    print(sitenames)
   
if __name__ == '__main__':
    main()