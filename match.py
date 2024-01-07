def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number" # _ It servers as the wildcard case, and will be executed if all other cases are not true
print(weekday(3))
print(weekday(6))
print(weekday(7))
### Combined cases
def access(user):
    match user:
        case "admin" | "manager": return "full access"
        case "guest" : return "limited access"
        case _: return "no access"
print(access("user"))
print(access("guest"))
print(access("admin"))
### List as the argument
def greeting(details):
    match details:
        case [time,name]:
            return f"Good {time} {name}!"
        case [time, *names]:
            msg = ''
            for name in names:
                msg += f'Good {time} {name}!\n'
            return msg
print(greeting(["Morning", "Hieu"]))
print(greeting(["Afternoon", "Hieu"]))
print(greeting(["Morning", "Hieu", "Cuong","hOANG"]))
### Using "if" in "case" clause
def instr(details):
    match details:
        case [amt, duration] if amt <10000:
            return amt*10*duration/100
        case [amt, duration] if amt >=10000:
            return amt*15*duration/100
print(instr([5000,5])) 
print(instr([15000,3])) 

