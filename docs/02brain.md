# Brain Simulation Modules
These classes represent portions of the brain that can then be fed to the Simulation class to run simulations
```mermaid
flowchart
A(Brain) --made up of--> B(Neuron Groups)
B --made up of--> C(Neurons)
```
## Class Daigram
```mermaid
classDiagram
class Neuron{
+id
+restingV
+thresholdV
+currentV
+fire()
+recievePotential()
+reset()
+update()
}
class NeuronGroup{
+name
+id
+neurons[]
+update()
+stimulateRandom()
+countSpikes()
}
class Brain{
+neuronGroups[]
+update()
+stimulate()
}

NeuronGroup <|.. Brain
Neuron <|.. NeuronGroup
```
## Flow of Events
When the brain is updated it stimulates various neuron groups. A neuron group contains multiple individual neurons. When a neuron group is stimulated it individually updates each neuron possibly cauing them to fire.