lacz-operon
===========

You can skip the next four paragraphs if you want.

During the final days of World War II, Adolf Hitler ordered several high-profile German microbiologists to initiate work on a top-secret project to halt the impeding Allied advance on Berlin. Codenamed "Projekt Aufguss" (which roughly translates to "Project Infusion"), these scientists used their knowledge of the lac operon to create an army of supersoldiers that could reuplse the Allied armies and retake Europe.

It was a well-known fact that roughly 83% of all German soldiers suffered from lactose intolerance. In an unfortunate coincidence, German army food was high in lactose - a single ration included a half-pound of hard cheese and enough powdered milk to make a liter of flatulence-inducing drink. As a result, morale throughout the war was consistently low due to unusually high concentrations of methane around army units. Projekt Aufguss' goal was to turn this weakness into a strength. If the lactose in milk could be broken down, morale would greatly increase. In addition, the hydrolysis of lactose yields glucose, a sugar known to enhance brain function. At the time, it was known that E. coli in the gut could digest lactose, and German scientists worked around the clock to increase the rate of digestion. It quickly became apparent that enzymes required to break down lactose in E. coli were regulated by various mechanisms: inducer proteins, repressor proteins, constitutive mutants. These were utilized to great effect in E. coli, which were then given to test subjects. Early tests were promising: soldiers that could digest lactose in large amounts had enhanced decision-making skills while enjoying flatulence levels 94% lower than their peers'.

Unfortunately for the experiment, Allied troops reached the laboratory where the experiments took place before they could be finished. The vast majority of the E. coli samples were destroyed, but a trio of French privates found a single sample still untouched in the laboratory's private wine celler when they were looking for a celebatory drink. Their names? Francois Jacob, Jacques Monod, and Andre Lwoff, winners of the 1965 Nobel Prize in Physiology.


I'd be lying if I said I spent more time on the story than on the program. At least I spent more time writing the story than writing the problem generator.


---------------------------------------------------
| lac operon problem generator and quizzer thingy |
|   version 0.1                                   |
---------------------------------------------------

This program takes predefined problems from geneReg.txt and solves the problems. The program can be used to check work, or to quiz oneself. The program can also give hints to each of the problems. A problem generator is included in case more problems are needed (geneReg.txt comes with 100 randomly-generated problems).

Each problem is stored in a 10-digit number. The first digit corresponds to the the I gene in the first chromosome, the second degit corresponds to the P gene in the second chromosome, and so on until the sixth digit, which corresponds to the I gene in the second chromosome. THe following values are used to denote a genotype:

I: S + - / 2 1 0
P: + - / 1 0
O: C + / 2 1
Z: + - / 1 0
Y: + - / 1 0


For example, a problem that is written as 1111111111 will have the following genotype:
  I+ P+ O+ Z+ Y+ / F' I+ P+ O+ Z+ Y+

On the other hand, 2010101210 will have the following genotype:
  IS P- O+ Z- Y+ / F' I- P+ OC Z+ Y-

For questions, feedback, hatemail, or anything else, contact me at errheller@gmail.com.

I spent way too much time on this, although I guess I really know the logic behind this stuff now. Hope it helps someone as it helped me!

Kyle Wong - 02:47 11-22-14
