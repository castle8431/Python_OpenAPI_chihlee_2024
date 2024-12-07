from pprint import pprint #為了看dict好看一點
import tools

def main():
    data:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')
    pprint(data)

if __name__ == '__main__':
    main()