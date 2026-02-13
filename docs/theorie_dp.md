# Theorie: Design Patterns

## Scenario:
Choose 2 Design Patterns of your choice and explain them in your own words. Not too much details, explain  
the problem and the solution.

## Answer:  
1. Strategy Pattern  
The main problem when we want to develop something is wanting to use one method thinking it is easier. But  
if we use too many if-else statements the code becomes messy and hard to test. The solution would be to use  
Strategy Pattern. It solves our problem by using different algorithms into separate classes, each class   
implements the same interface. We therefore have concrete classes and we can now add new strategies without  
changing the code, we can test each strategy independently.

2. Observer Pattern  
The Observer Pattern can come in handy in situations like this, where we for example want to build a shopping  
cart which needs to update multiple things at once simultanously, where all of the elements are dependent on  
eachother. Instead of writing many lines of code we can simply use the observer pattern can create a notification  
system, where the subject maintains a list of observers instead of having to change it one by one.  
Each observer implements a simple interface with an update method. When something changes in the cart, it  
notifies all observers by calling their update method.The biggest perk here too is not having to touch the  
subject code.
