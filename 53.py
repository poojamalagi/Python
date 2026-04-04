# Print numbers from 1 to 20, but skip all even numbers.
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(f"odd number{i}")
    i=i+1
    