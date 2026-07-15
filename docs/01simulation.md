# Simulation
Run a simulation using components in a given time frame
```mermaid
flowchart
    A[Simulation] --> B(Configuration)
    A --> C(SimulationClock)
    A --> D(Logger)
    A --> E(Components)
```
## Class Diagram
```mermaid
classDiagram
    class Simulation{
    +configuration
    +clock
    +logger
    +components[]
    +run()
    +update()
    +add_component(component)
    } 
    class Configuration{
        +configs
    }
    class Component{
        +update()
    }
    class Logger{
        +log(message)
    }
    class SimulationClock{
        +current_time
        +get_current_time()
        +step(delta_time)
    }
    Configuration <|.. Simulation
    SimulationClock <|.. Simulation
    Logger <|.. Simulation
    Component <|.. Simulation

```
## Chain of Events
When the simulation begins it updates all components and logs all updates. Then the clock is updated and the simulation continues until the total duration is reached.