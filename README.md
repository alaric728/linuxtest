# Linux Code Test: 'Factoids'

## Overall Requirements
Create an apt repo package which, when installed, allows you to type a command which displays a fact about one of your extracurricular interests. Please use this as a chance to showcase your personality.

This command should be invoked via a simple command such as `factoid` and will then display a randomly chosen factoid. See simple example below

```
# factoid
> Hulk Hogan vs Andre the Giant was featured at WrestleMania 3
```

The point of this test is to understand how you approach a technical problem. The way you code is just as important as your solution.

We expect this test to take you about 4 - 8 hours. Given that most people are busy, We'd like to hear back from you within 72 hours of starting.

#### As soon as you begin:
* [ ] Fork this repository into a public repository on your github/etc account

#### While working on this, please:
* [ ] Commit early and often. I'll likely be following along with your progress.

#### Upon completing this, please post to us:
* [ ] A link to your git repository such that we may view your code.
* [ ] A link to somewhere where we may download and install your package

## Requirements

The underpinnings of the Commands functionality may be written in whatever language you choose, so long as it is operable on apt repo (beware libraries that do not come installed by default)

#### Command Line Interface
* [ ] Using the command `factoid` should return to you a randomly chosen fact. 
* [ ] Using the command `factoid -n 1` (with flag n specified and number passed) should show you the nth factoid in the bunch
  * [ ] Please handle a number flag that is out of range appropriately

#### Packaging 
* [ ] Provide use of this command via a apt repo style package. 
* [ ] The package must function on any currently available OS of your choosing. 

#### Reproducibility
* [ ] Use a make file to create your package

## BONUS

If you're too cool for school and knocked all the above out already, consider adding some improvements to what you've made.

### Suggestions for improvements
* [ ] How about color the output using an external dependency?
* [ ] Edit this ReadMe with new suggestions for how to improve this code test
