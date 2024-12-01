
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        lines = file.read().splitlines()
        
    list1 = [int(line.split("   ")[0]) for line in lines]
    list2 = [int(line.split("   ")[1]) for line in lines]
    
    list1.sort()
    list2.sort()
    
    print(f'These are the sorted lists:\n{list1}\n{list2}')
    
    total = 0
    for nb in list1:
        count = list2.count(nb)
        total += nb * count
    
    print(f'The total is: {total}')

if __name__ == '__main__':
    main()