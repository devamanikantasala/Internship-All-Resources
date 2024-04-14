#Exercises Level 1
#Task 1 : Find the length of the set it_companies
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"};
print("The Length of it_companies : ", len(it_companies));

#Task 2: Add Twitter to it_companies
it_companies.add("Twitter");
print(it_companies);

#Task 3: Insert multiple IT companies at once to the set it_companies;
for item in ["Wipro", "Amazon AWS", "Meta", "Silicon Valley", "NVIDIA"]:
    it_companies.add(item);
print(it_companies);

#Task 4: Remove one of the companies from the set it_companies
it_companies.remove("Facebook");
print(it_companies);

#Task 5: What is the difference between remove() and discard()
# remove() method raises a KeyError if there is no specified item in the set.
# discard() method don't raise a KeyError if the specified item is not found.

#trying remove() method
try:
    it_companies.remove("Facebook"); #raises an KeyError
    print("Facebook was removed successfully!");
except Exception as e:
    print("Facebook is not in the set, and it is not possible to remove!\nError: ", e); #This line executes

#trying discard() method
try:
    it_companies.discard("Facebook"); #doesn't raises an KeyError
    print("Facebook was removed successfully! or already removed!"); #This line executes
except Exception as e:
    print("Facebook is not in the set, and it is not possible to remove!\nError: ", e);
