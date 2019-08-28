# Linux Code Test: 'Steam Locomotion'

## Overall Requirements
Create a copy or fork of sl, and extend the functionality and create a package for the program. After installing the package, you should be able to type `sl` and at least see the following:

![](demo.gif)

You may use as much or as little from the sl source as you wish, and can program in whatever language you choose (as long as it isn't Ook!).

The additional functionality you will provide is that `sl` will no longer show the same train you see above every time but rather your own flavor, or assortment of flavors! 

Make the `sl` command display a locomotive randomly from a set of possible locomotives, and add an additional option `-n [0-9]*` which takes an integer corresponding to the nth locomotive, and displays the nth locomotive to terminal.

The point of this test is to understand how you approach a technical problem. The way you code is just as important as your solution.

We expect this test to take you about 4 - 8 hours. Given that most people are busy, We'd like to hear back from you within 72 hours of starting.

You can find the sl source here: https://github.com/mtoyoda/sl
And some ascii art fun here: https://www.asciiart.eu/

#### As soon as you begin:
* [ ] Fork this repository into a public repository on your github/etc account

#### While working on this, please:
* [ ] Commit early and often. We'll likely be following along with your progress.

#### Upon completing this, please post to us:
* [ ] A link to your git repository such that we may view your code.
* [ ] A link to somewhere where we may download and install your package

## Requirements

The underpinnings of the Commands functionality may be written in whatever language you choose, so long as it is operable after installing the package (beware libraries that do not come installed by default)

#### Command Line Interface
* [ ] Using the command `sl` should return to you a randomly chosen fact. 
* [ ] Using the command `sl -n N` (with option n specified and argument integer passed) should show you the Nth locomotive in the bunch
* [ ] Please handle options that are not defined or malformed

#### Packaging 
* [ ] Provide use of this command via a apt repo style package. 
* [ ] The package must function on any currently available OS of your choosing. 

#### Reproducibility
* [ ] Use a make file to create your package

## BONUS

If you're too cool for school and knocked all the above out already, consider adding some improvements to what you've made.

### Suggestions for improvements
* [ ] How about having the program pull random ascii art from a file or folder?
* [ ] Edit this ReadMe with new suggestions for how to improve this code test
