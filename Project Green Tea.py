#A semi-website project on Green tea
Topics = ['Definition', 'Evolution/History: The Birth of Green Tea', 'Tradition till Date', 'Why You Should Switch To Green Tea: Health Benifits', 'Get Started Now : How You Can Make a Simple Herbal Tea', 'My Personal Experience with Green Tea in My Everyday Life'] 
print(Topics)

X = ("\n Definition = H || Evolution = E,\n Tradition = R || Health Benifits = B,\n Make Herbal Tea = A || Personal Experience = L.\n Exit = 0")
print(X.upper())

X = input("\nMake a choice : H / E / R / B / A / L  / 0\n")

if X == 'H':
    print('Definition')
elif X == 'E':
    print('Evolution/History: The Birth of Green Tea')
elif X == 'R':
    print('Tradition till Date')
elif X == 'B':
    print('Why You Should Switch To Green Tea: Health Benifits')
elif X == 'A':
    print('Get Started Now : How You Can Make a Simple Herbal Tea')
elif X == 'L':
    print('My Personal Experience with Green Tea in My Everyday Life')
elif X == 'T':
    exit()
else:
    print("Please Read the instructions Carefully")
    X = input("\nMake a choice : H / E / R / B / A / L  / T\n")


