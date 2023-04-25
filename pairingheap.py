import csv

symptoms_dict = dict()
with open("project file 2.csv", 'r') as file:
    symptoms_file = csv.reader(file)
    next(symptoms_file)
    for symptoms,priority in symptoms_file:
        symptoms_dict[symptoms] = priority #{symptom: priority}

class Patient():
    def __init__(self, name, age = None, symptoms = "") -> None:
        self.name = name
        self.age = age
        self.symptoms = symptoms.split(", ")
        self.priority = self.calculate_priority(self.symptoms)
    
    def calculate_priority(self, symptoms_lst: list) -> int:
        priority = 0
        for symptom in symptoms_lst:
            priority += int(symptoms_dict[symptom]) #for every symptom, adds its priority in patients priority
        return priority
    
    def update_symptoms(self, symptoms_lst:str):
        self.symptoms = symptoms_lst.split(", ")
        self.priority = self.calculate_priority(self.symptoms)
    

class Node():
    def __init__(self, patient:Patient = None):
        self.sibling = None
        self.left_child = None
        self.parent = None
        self.patient:Patient = patient
    
        
class PairingHeap():
    def __init__(self):
        self.root:Node = None #initializing a heap with root none

    def MakeHeap(self, key:Patient): #makes a new heap with root having the value equal to the given key
        new = PairingHeap()
        new.root = Node(key)
        return new.root #returns the root of the node

    def insert(self, key:Patient):
        if self.root == None: #if this is the first node to insert then make a new heap and make it the root of the heap
            self.root = self.MakeHeap(key)
        else:
            new_root = self.MakeHeap(key)  #if the heap is not empty then create a new heap with the new key value
            self.Merge(self.root, new_root) #merge the already existing hep with the new created one
        
    def Merge(self, heap1:Node, heap2:Node):#takes the roots of both heaps; only roots because only the pointers of the root need to be changed
        if heap1 is None:
            return heap2
        if heap2 is None:
            return heap1
        if heap2.patient.priority > heap1.patient.priority: #to make sure that heap1 is the heap with maximum value; this makes further execution easy
            heap1, heap2 = heap2, heap1
        #updating the pointers; 
        heap2.sibling = heap1.left_child
        heap1.left_child = heap2
        heap2.parent = heap1
        heap1.sibling = None
        self.root = heap1
        return self.root

    def FindMax(self): #Returns the patient with heighest priority, doesnot remove it
        return (self.root.patient.name, self.root.patient.age, self.root.patient.symptoms)

    def DeleteMax(self):#fixing needed!!
        if not self.root:
            return None
        if self.root.left_child == None:
            return None
        max_value = self.root.patient.name
        children = []
        child = self.root.left_child
        while child:
            children.append(child)
            child = child.sibling
        for i in range(0,len(children)-1):
            children[i+1] = self.Merge(children[i], children[i+1])
            children[i] = None
        self.root = children[i+1]
        return max_value

    def find(self, name:Node):
        node = self.root
        while node.left_child is not None:
            if node.patient.name == name:
                return node
            node = node.left_child
            while node.sibling is not None:
                node = node.sibling
                if node.patient.name == name:
                    return node
        return None
    
    def update_priority(self, name:Node, symptoms:str):
        patient_node = self.find(name)
        if patient_node is not None:
            patient_node.patient.update_symptoms(symptoms)
            patient_node.parent.left_child = None
            patient_node.parent = None
            self.Merge(self.root, patient_node)


    # def decrease_key(self, node, new_value):
    #     node.value = new_value
    #     if node.parent is None:
    #         return
    #     if node.value < node.parent.value:
    #         parent = node.parent
    #         node.parent = None
    #         parent.children.delete(node)
    #         self.root = self.Merge(self.root, node)
    #         self.decrease_key(parent, node.value)

    def display_node(self,node:Node): 
            count = 1
            print(node.patient.name, str(node.patient.priority))
            while node.left_child is not None:
                node = node.left_child
                print("left_child", node.patient.name, str(node.patient.priority))
                count+=1
                while node.sibling is not None:
                    node = node.sibling
                    print("sibling", node.patient.name, str(node.patient.priority))
                    count+=1
            return count
        
    def display(self):
        if not self.root:
            print("Empty heap")
            return
        print(self.display_node(self.root))
         

patients_data = PairingHeap()
with open("project file 1 (1).csv", 'r') as file:
    patients_file = csv.reader(file)
    next(patients_file)
    for name, age, symptoms in patients_file:
        new_patient = Patient(name, age, symptoms) #for every line, a new patient object is created and appended in a lst
        patients_data.insert(new_patient)

patients_data.display()
patients_data.update_priority('Charlotte', "Diarrhea, Abdominal pain, Constipation")
patients_data.display()
# patients_data.decrease_key('Joseph', 100)
patients_data.display()