# Poster: Evolutionary Design of Particle Swarms using Celery and Python.

## Title

- Multiprocess Evolutionary Algorithms and Simulation using Python and Celery
- Pygame, Celery, and Numpy - A Perfect Stack for Evolutionary Algorithms
- Computationally Intensive Genetic Algorithms with Python and Celery
- Particles at War: Simulating Evolution with Python and Celery
- Computationally Intensive Genetic Algorithms Made Easy with Pygame, Celery, and Numpy
- _Experimentation Using Genetic Algorithms Made Easy with Pygame, Celery, and Numpy_

We need a better title.

## Category

**Science**

## Python Level

**Intermediate**

## Description

_If your talk is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters._

Genetic algorithms are efficient optimizers inspired by biological evolution and widely used in academic research. However, GAs can be computationally intensive, particularly for simulation. In this poster we detail how Python tools, particularly Pygame, Celery, and Numpy were used in scientific experimentation that took days to compute the evolution of movement behaviors of a particle swarm.


## Detailed Abstract

_Detailed description. Will be made public if your talk is accepted._

Evolutionary computation is inspired by biological evolution and utilizes metaphors of reproduction, crossover, recombination, mutation, and selection by fitness to perform optimization. Evolutionary techniques are primarily used in academia, but also in industrial design where they are used to optimize the parameters or specifications of physical objects. Of note is a quarter-sized antenna that was designed by evolutionary algorithms (EAs) and whose design was far better than similar human designs (that antenna is now used in a variety of satellites).

The idea that genetic and evolutionary algorithms can be used for computational creativity and design is an interesting one. More specifically, we considered whether or not we could use EAs to design a particle swarm system that outperformed a human designed one. The result was a research project that lasted several months and resulted in a publication -- yes, EAs can in fact outperform human design for these types of applications!

However, actually conducting the experimentation required a lot of computation - the result was achieved after evolution of 80 generations that took over 70 hours to complete! The use of Python tools to aid in our scientific investigation was critical, or we would have never had a result. We used Celery to multiprocess the evolution so that 16 simulations were running simultaneously on an m1.2xlarge Amazon EC2 instance. We utilized Numpy and Scikit-Learn to perform vector and matrix computations as efficiently as possible, and finally we used Pygame to visualize the simulation and study the results in real time.

In this poster, we hope to show how Python tools were critical to our research. The clever application of Python to research extends beyond SciPy - it requires multiprocessing, simulation, visualization and more!

## Additional Notes

_Anything else you'd like the program committee to know when making their selection: your past speaking experience, open source community experience, etc._

This poster is based on an academic paper that was submitted to IEEE SSCI in 2014:

Bengfort, Benjamin, et al. "[Evolutionary design of self-organizing particle systems for collective problem solving.](http://cs.umd.edu/~bengfort/research/evolutionary-design-of-particle-swarms/)" Swarm Intelligence (SIS), 2014 IEEE Symposium on. IEEE, 2014.

Note that the [slides](http://www.slideshare.net/BenjaminBengfort/evolutionary-design-of-swarms-ssci-2014), [paper](http://cs.umd.edu/~bengfort/papers/evolutionary-design-swarms.pdf), and [Github repository](https://github.com/mclumd/swarm-simulator) for the work are all available at the link in the citation. Because the scientific community is attracted to Python tools for their work and because Python hackers are using ever more machine learning techniques and genetic algorithms, I wanted to present this work to specifically show how Python and science are used in meaningful ways. The poster therefore will focus on the Python (Celery, Pygame, Numpy) and not necessarily the academic contribution that was presented previously.  

My past speaking experience includes O'Reilly Strata, Data Science DC, IEEE SSCI (where the scientific work for this project was presented), and IEEE WCNC. I am a board member of Data Community DC - a not-for-profit organization of 6 meetups in the DC area that focus on data science. I'm involved in a number of open source projects and attempt to make all my academic work open source whenever I can.

Additionally, if this is of interest, I'm happy to resubmit this topic as a talk rather than a paper.

## Additional Requirements

_Please let us know if you have any specific needs (A/V requirements, multiple microphones, a table, etc). Note for example that 'audio out' is not provided for your computer unless you tell us in advance._

The project includes a simulation that was written using Pygame that demonstrates the various stages of evolution - a screen with an HDMI hookup and a table would be useful to present the simulation and computational techniques.  

The poster will have lots of visual elements and will be printed on a glossy 40" x 30". We would need to know ahead of time if we should mount it on form board (therefore an easel will be required) or if there is a non-destructive way of mounting the poster.
