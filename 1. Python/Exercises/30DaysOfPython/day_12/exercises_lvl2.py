#Task 1:
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (Six hexadecimal numbers written after #. Hexadecimal numerical system is made out of 16 symbols
#0-9 and first 6 letters of the alphabet -- a-f.)
from random import random, randint;
import string as st;

def list_of_hexa_colors():
    n = int(input("Enter the number of colors do you want? : "));
    characters = st.digits + st.ascii_lowercase[0:6] + st.ascii_uppercase[0:6];
    i = 0;
    hexa_colors_list = []
    while(i < n):
        j = 0;
        color = "#"
        while (j < 6):
            random_index = randint(0, len(characters)-1);
            color += characters[random_index];
            j += 1;
        hexa_colors_list.append(color);
        i += 1;
    print("Hexa Colors : ", hexa_colors_list);

print("Task 1: Hexa Colors list.");
list_of_hexa_colors();

#Task 2:
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array

def list_of_rgb_colors():
    n = int(input("Enter the number of colors do you want? : "));
    rgb_colors_list = []
    for i in range(n):
        value_1 = randint(0, 255);
        value_2 = randint(0, 255);
        value_3 = randint(0, 255);
        string = f'rgb({value_1}, {value_2}, {value_3})';
        rgb_colors_list.append(string);
    print("RGB colors : ", rgb_colors_list);

print("Task 2: RGB Colors List");
list_of_rgb_colors();

#Task 3:
# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_code, n):
    if(color_code.lower() != 'hexa' and color_code.lower() != 'rgb'):
        print(f"Invalid Color Code or {color_code} is not available!");
        return;
    elif(color_code.lower() == 'hexa'):
        hexa_colors_list = [];
        print("Printing Hexa Colors --", n);
        characters = st.digits + st.ascii_lowercase[0:6] + st.ascii_uppercase[0:6];
        i = 1;
        while(i <= n):
            j = 0;
            color = '#';
            while(j < 6):
                random_index = randint(0, len(characters)-1);
                color += characters[random_index];
                j += 1;
            hexa_colors_list.append(color);
            i += 1;
        print(hexa_colors_list);
        return;
    else:
        rgb_color_list = [];
        i = 1;  
        print("Printing RGB Colors --", n);
        while(i <= n):
            value_1 = randint(0, 255);
            value_2 = randint(0, 255);
            value_3 = randint(0, 255);
            string = f'rgb({value_1}, {value_2}, {value_3})';
            rgb_color_list.append(string);
            i += 1;
        print(rgb_color_list);
        return;
print("Task 3: Color Generator Hexa or RGB");
generate_colors('hexa', 3);
generate_colors('RGB', 4);
generate_colors('HSL', 3);
