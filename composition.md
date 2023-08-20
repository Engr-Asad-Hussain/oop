## Composition: Favour composition over inheritance

Many of the design patterns in the ***Gang of Four Design Patterns*** book are based on the principle favour composition over inheritance. But what does that mean? Let's find out. If you want to separate responsibilities, create code with higher cohession, there's a couple of ways to do it. 
  1. One way to do it is inheritance. So instead of putting everything in one single big class, you would create a class hierarchy of classes and subclasses, where you would put certain things in a subclass so that it would be separated from the main class. 
  2. Another way you can do is composition. That means that you are basically using separate classes to represent separate things in the application. And then each of these classes use each other in some meaningful way. 

Its basically the difference between the ```is-a relationship``` which is inheritance and ```has-a relationship``` which is composition; allow you to separate responsibilities. Consider a following advanced example of employee management system.

```py
class HourlyEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        pay_rate: float = 0,
        hours_worked: int = 0,
        employer_cost: float = 1000,
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    def compute_pay(self):
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )
```
We have an hourly employee who's paid based on the number of work hours. The hourly employee have some personnel data like the ```name``` and ```id```, we have a part that's about ```commission```. So if an employee lands a number of contract, the employee gets a commission, we have ```pay_rate```, number of ```hours worked```, and there is a kind of fixed ```employee cost```. And then we have ```compute pay``` method that actually computes how much the employee should be paid based on these values here.

```py
class SalariedEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def compute_pay(self):
        return (
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )
```
Salaried employee that gets a fixed monthly salary. Salaried employees quite to similar to ```HourlyEmployee```. It also has a ```name```, ```id```, it also has a commission structure. But there is a ```monthly salary``` and a ```percentage``` of time that the employee works. And then this is the ```compute pay``` method. 

```py
class FreelancerEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        pay_rate: float = 0,
        hours_worked: int = 0,
        vat_number: str = "",
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.vat_number = vat_number

    def compute_pay(self):
        return (
            self.pay_rate * self.hours_worked + self.commission * self.contracts_landed
        )
```
And we have a freelancer. Freelancer is not actually an employee. But if we consider an employee as a person that gets paid by a company for work performed, and it kind of fits under that same umbrella. Freelancer also has ```name``` and ```id```, ```commission```, ```pay rate``` and ```hours worked```. And then we have an additional ```VAT number``` for taxes. 

```py
def main():
    henry = HourlyEmployee(name="Henry", id=1002, pay_rate=50, hours_worked=100)
    print(
        f"`{henry.name}` worked for `{henry.hours_worked}` hours and earned `${henry.compute_pay()}`."
    )

    sarah = SalariedEmployee(
        name="Sarah", id=2031, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"`{sarah.name}` landed `{sarah.contracts_landed}` contracts and earned `${sarah.compute_pay()}`."
    )

if __name__ == "__main__":
    main()
```
In the main function where we create a couple of these employees print out some information. And this is what happens when I run this example.




Now, let's analyse this





> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
- [ ] \(Optional) Open a followup issue