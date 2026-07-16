# Brain Simulation Modules
These classes represent portions of the brain that can then be fed to the Simulation class to run simulations
## Composition of the Brain
```mermaid
flowchart
A(Brain) --made up of--> B(Neuron Groups)
B --made up of--> C(Neurons)
C --> D(Synapse)
D --> C
```
## Neuron Communication
```mermaid
flowchart
A(Neuron A) --releases signal--> B(Synapse) --transfers signal--> C(Neuron B)
```
## Class Daigram
```mermaid
classDiagram
class Neuron{
+id
+restingV
+thresholdV
+currentV
+outgoingSynapses[]
+fire()
+recieveSignal()
+reset()
+update()
+addSynapse()
+removeSynapse()
}
class NeuronGroup{
+name
+id
+neurons[]
+update()
+addNeuron()
+removeNeuron()
}
class Brain{
+neuronGroups[]
+update()
}
class Synapse{
    +targetNeuron
    +weight
    +delay
    +transmit()
}

NeuronGroup <|.. Brain
Neuron <|.. NeuronGroup
Neuron <|.. Synapse
Synapse <|.. Neuron
```
## Flow of Events
When the brain is updated it updates the various neuron groups it contains. A neuron group contains multiple individual neurons. When a neuron group is updated it individually updates each neuron possibly cauing them to fire and stimulate other neurons via a synapse.