import csv

symptoms_dict = dict()
with open("project file 2.csv", 'r') as file:
    symptoms_file = csv.reader(file)
    next(symptoms_file)
    for symptoms,priority in symptoms_file:
        symptoms_dict[symptoms] = priority #{symptom: priority}

class Patient():
    def __init__(self, name, age, symptoms, id = 0) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.symptoms_str = symptoms
        self.symptoms = symptoms.split(", ")
        self.priority = self.calculate_priority(self.symptoms)
    
    def calculate_priority(self, symptoms_lst: list) -> int:
        priority = 0
        for symptom in symptoms_lst:
            priority += int(symptoms_dict[symptom]) #for every symptom, adds its priority in patients priority
        return priority
    
    def update_symptoms(self, symptoms_lst:str):
        self.symptoms_str = symptoms_lst
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
        self.inserts = 0

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
        return (self.root.patient.id, self.root.patient.name, self.root.patient.age, self.root.patient.symptoms)

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

    def find(self, id):
        node = self.root
        if node.patient.id == id:
            return node
        while node.left_child is not None:
            node = node.left_child
            if node.patient.id == id:
                return node
            while node.sibling is not None:
                node = node.sibling
                if node.patient.id == id:
                    return node
        return None
    
    def update(self, id, name = "", age = 0, symptoms = ""):
        patient_node = self.find(id)
        if patient_node is not None:
            patient_node.patient.update_symptoms(symptoms)
            patient_node.patient.age = age
            patient_node.patient.name = name
            if patient_node.parent:
                patient_node.parent.left_child = None
            patient_node.parent = None
            self.Merge(self.root, patient_node)
        return patient_node.patient

    def display_node(self,node:Node): 
        all_patients = [node.patient]
        while node.left_child is not None:
            node = node.left_child
            all_patients.append(node.patient)
            while node.sibling is not None:
                node = node.sibling
                all_patients.append(node.patient)
        return all_patients
        
    def display(self):
        if not self.root:
            return
        return (self.display_node(self.root))
         

patient_heap = PairingHeap()
with open("project file 1 (1).csv", 'r') as file:
    patients_file = csv.reader(file)
    next(patients_file)
    for name, age, symptoms in patients_file:
        patient_heap.inserts += 1
        new_patient = Patient(name, age, symptoms, patient_heap.inserts) #for every line, a new patient object is created and appended in a lst
        patient_heap.insert(new_patient)

# print(patients_data.FindMax())
# patients_data.update_priority('Charlotte', "Diarrhea, Abdominal pain, Constipation")
# print(patients_data.display())
# # patients_data.decrease_key('Joseph', 100)
# patients_data.display()