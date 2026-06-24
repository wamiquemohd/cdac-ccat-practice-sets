#!/usr/bin/env python3
"""
Generates updated index.html with 4 practice sets, set-selector UI,
Section C support (Set 3), and updated branding.
Run: python3 generate.py
"""
import base64, re, json, sys

HTML_PATH = '/Users/wamique/Claude Code/ccat-mock-test/index.html'
KEY = [0x4D, 0x77, 0x51, 0x7C, 0x63, 0x58, 0x4F, 0x52, 0x71, 0x39]

def encode_ak(answers):
    raw = bytes([(a + 65) ^ KEY[i % len(KEY)] for i, a in enumerate(answers)])
    return base64.b64encode(raw).decode()

def qs_to_js(questions):
    items = []
    for idx, (sec, cat, q, opts, ans) in enumerate(questions, 1):
        exp_text = f"Correct answer is {chr(65+ans)}: {opts[ans]}"
        d = {"id": idx, "s": sec, "cat": cat, "q": q, "o": opts, "exp": exp_text}
        items.append(json.dumps(d, ensure_ascii=False))
    return ',\n  '.join(items)

# ================================================================
#  SET 1 — Normal (100 questions)
# ================================================================
s1_data = [
  ['A','English – Vocabulary','Choose the SYNONYM of BENEVOLENT',['Kind','Cruel','Indifferent','Arrogant'],0],
  ['A','English – Vocabulary','Choose the ANTONYM of VERBOSE',['Concise','Lengthy','Wordy','Talkative'],0],
  ['A','English – Vocabulary','Choose the SYNONYM of DILIGENT',['Lazy','Hardworking','Careless','Reckless'],1],
  ['A','English – Vocabulary','Choose the ANTONYM of TRANSPARENT',['Opaque','Clear','Obvious','Visible'],0],
  ['A','English – Vocabulary','Choose the SYNONYM of PRUDENT',['Rash','Wise','Foolish','Ignorant'],1],
  ['A','English – Grammar','Fill in the blank: She ______ to the market yesterday.',['go','goes','went','gone'],2],
  ['A','English – Grammar','Identify the error: "He do not knows the answer."',['He','do not','knows','the answer'],1],
  ['A','English – Grammar','Fill in the blank: Neither the students nor the teacher ______ present.',['were','are','was','been'],2],
  ['A','English – Grammar','Choose the correct sentence:',['She is more smarter than him.','She is smarter than him.','She is most smarter than him.','She is smarter then him.'],1],
  ['A','English – Grammar','Fill in the blank: The committee ______ reached a unanimous decision.',['have','has','had been','were'],1],
  ['A','English – Reading Comprehension','Read the following passage:\n\nCloud computing is the delivery of computing services including servers, storage, databases, networking, software, analytics and intelligence over the Internet to offer faster innovation, flexible resources and economies of scale. Users typically pay only for the services they use, helping to lower operating costs, run infrastructure more efficiently, and scale as business needs change. Cloud computing can be broadly divided into three models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). These models differ in the level of control, flexibility, and management the cloud provider handles. Major providers include Amazon Web Services, Microsoft Azure, and Google Cloud Platform.\n\nWhat is the main topic of the passage?',['Internet security','Cloud computing services and models','Database management','Network infrastructure'],1],
  ['A','English – Reading Comprehension','According to the passage, which of the following is NOT mentioned as a cloud computing service?',['Storage','Networking','Artificial Intelligence','Analytics'],2],
  ['A','English – Reading Comprehension','What are the three cloud service models mentioned in the passage?',['IaaS, PaaS, SaaS','Public, Private, Hybrid','AWS, Azure, GCP','Server, Client, Peer'],0],
  ['A','English – Reading Comprehension','According to the passage, how do users typically pay for cloud services?',['Monthly subscription only','Only for the services they use','Annual flat fee','Per user license'],1],
  ['A','English – Reading Comprehension','Which of the following is cited as a benefit of cloud computing in the passage?',['Increased hardware costs','Slower innovation','Economies of scale','Fixed resource allocation'],2],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: A person who hates mankind',['Misogynist','Philanthropist','Misanthrope','Narcissist'],2],
  ['A','English – Para-jumble & One-word Substitution','Arrange the sentences in order:\nP: He opened the door.\nQ: He heard a knock.\nR: A stranger stood outside.\nS: He was reading a book.',['SQPR','SPQR','SQRP','PQRS'],0],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: Words written on a tomb',['Epilogue','Epitaph','Epigraph','Elegy'],1],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: One who can speak two languages',['Polyglot','Bilingual','Linguist','Multilingual'],1],
  ['A','English – Para-jumble & One-word Substitution','Arrange: P: The exam was tough. Q: Students studied hard. R: Results were excellent. S: Everyone celebrated.',['QPRS','PQRS','RSPQ','SQRP'],0],
  ['A','Quantitative Aptitude','A can do a work in 10 days and B can do it in 15 days. In how many days can they finish it together?',['5','6','8','12'],1],
  ['A','Quantitative Aptitude','A shopkeeper buys an item for Rs.400 and sells it for Rs.500. Find the profit percentage.',['20%','25%','15%','10%'],1],
  ['A','Quantitative Aptitude','Find the Simple Interest on Rs.5000 at 8% per annum for 3 years.',['Rs.1000','Rs.1200','Rs.1400','Rs.1500'],1],
  ['A','Quantitative Aptitude','The ratio of two numbers is 3:5. If their sum is 160, find the larger number.',['60','80','100','120'],2],
  ['A','Quantitative Aptitude','What is 15% of 240?',['36','32','40','24'],0],
  ['A','Quantitative Aptitude','A train 120m long passes a pole in 12 seconds. Find its speed in km/h.',['36','40','42','48'],0],
  ['A','Quantitative Aptitude','In how many ways can 5 books be arranged on a shelf?',['60','100','120','24'],2],
  ['A','Quantitative Aptitude','What is the probability of getting at least one head when a fair coin is tossed twice?',['1/4','1/2','3/4','1'],2],
  ['A','Quantitative Aptitude','Find the Compound Interest on Rs.1000 at 10% per annum for 2 years.',['Rs.200','Rs.210','Rs.220','Rs.100'],1],
  ['A','Quantitative Aptitude','A mixture of 60 litres has milk and water in ratio 2:1. How much water must be added to make ratio 1:1?',['10','20','30','60'],1],
  ['A','Quantitative Aptitude','If the cost price of 12 items equals the selling price of 10 items, find the profit percentage.',['15%','20%','25%','16.67%'],1],
  ['A','Quantitative Aptitude','Two pipes A and B can fill a tank in 20 and 30 minutes. Both open together, when will the tank be full?',['10 min','12 min','15 min','25 min'],1],
  ['A','Quantitative Aptitude','A number when divided by 5 gives remainder 3 and when divided by 7 gives remainder 4. Find the smallest such number.',['18','53','32','28'],0],
  ['A','Quantitative Aptitude','In what ratio must water be mixed with milk costing Rs.12/litre to get mixture costing Rs.8/litre?',['1:2','2:1','1:1','3:1'],0],
  ['A','Quantitative Aptitude','Speed of a boat in still water is 15 km/h and stream speed is 3 km/h. Time to go 54 km downstream?',['3 hrs','4 hrs','2.5 hrs','3.5 hrs'],0],
  ['A','Reasoning','Find the next number: 2, 6, 12, 20, 30, ?',['42','40','44','36'],0],
  ['A','Reasoning','Find the next in series: AZ, BY, CX, DW, ?',['EV','EU','FV','EW'],0],
  ['A','Reasoning','If CAT = 3120, then what does DOG equal using same position scheme?',['4715','4175','41514','4157'],3],
  ['A','Reasoning','A is the brother of B. B is the mother of C. What is A to C?',['Father','Uncle','Grandfather','Brother'],1],
  ['A','Reasoning','Ravi walks 5 km North, turns right and walks 3 km, then turns right and walks 5 km. How far is he from start?',['3 km','5 km','8 km','0 km'],0],
  ['A','Reasoning','All roses are flowers. Some flowers are red. Which conclusion follows?\nI. Some roses are red.\nII. All flowers are roses.',['Only I','Only II','Both I and II','Neither I nor II'],3],
  ['A','Reasoning','Find the odd one out: 8, 27, 64, 100, 125',['27','100','125','64'],1],
  ['A','Reasoning','Pointing to a photo, Mohan says "She is the daughter of my grandfather\'s only son." Who is she to Mohan?',['Sister','Cousin','Mother','Daughter'],0],
  ['A','Reasoning','A clock shows 3:15. What is the angle between the minute and hour hands?',['0°','7.5°','15°','22.5°'],1],
  ['A','Reasoning','Find next: 1, 4, 9, 16, 25, ?',['30','36','49','35'],1],
  ['A','Reasoning','BDFH : ACEG :: JLNP : ?',['IKMO','KLMN','IKMQ','HIJK'],0],
  ['A','Reasoning','If FRIEND is coded as HUMJTK, how is CANDLE coded?',['EDRIRL','ECPFNG','EDRJRL','DCPFNG'],1],
  ['A','Reasoning','In a row of 40 students, Priya is 15th from the left and Sunil is 20th from the right. How many students are between them?',['4','5','6','7'],1],
  ['A','Reasoning','Find the missing number: 3, 7, 13, 21, 31, ?',['41','43','45','47'],1],
  ['A','Reasoning','A is twice as old as B. 10 years ago A was 3 times as old as B. What is B\'s current age?',['15','20','25','30'],1],
  ['B','Computer Fundamentals','What is the decimal equivalent of binary 11010?',['24','26','28','30'],1],
  ['B','Computer Fundamentals','Convert hexadecimal 2F to decimal.',['45','47','49','51'],1],
  ['B','Computer Fundamentals','Which gate outputs 1 only when all inputs are 1?',['OR','AND','NAND','NOR'],1],
  ['B','Computer Fundamentals','Simplify the Boolean expression: A + A\'B',['A + B','AB','A\'','A'],0],
  ['B','Computer Fundamentals','Which of the following is the universal gate?',['AND','OR','NAND','XOR'],2],
  ['B','C Programming','#include<stdio.h>\nint main(){\n  int x=5;\n  printf("%d", x++);\n  return 0;\n}\nWhat is the output?',['5','6','4','Error'],0],
  ['B','C Programming','#include<stdio.h>\nint main(){\n  int a=10, b=3;\n  printf("%d", a%b);\n  return 0;\n}\nWhat is the output?',['3','1','0','2'],1],
  ['B','C Programming','What will be the output?\n#include<stdio.h>\n#define SQ(x) x*x\nint main(){\n  printf("%d", SQ(3+1));\n  return 0;\n}',['16','7','13','10'],1],
  ['B','C Programming','What is the size of an int pointer on a 64-bit system?',['2 bytes','4 bytes','8 bytes','16 bytes'],2],
  ['B','C Programming','What will be the output?\nint a[]={1,2,3,4,5};\nprintf("%d", *(a+2));',['1','2','3','4'],2],
  ['B','C Programming','Which storage class has a lifetime throughout the program execution?',['auto','register','static','extern'],2],
  ['B','C Programming','What does malloc() return if memory allocation fails?',['0','NULL','-1','Garbage value'],1],
  ['B','C Programming','What is the output?\nint x=5;\nint *p=&x;\n*p=10;\nprintf("%d",x);',['5','10','Address of x','Error'],1],
  ['B','C Programming','Which bitwise operator can be used to check if a number is even or odd?',['&','|','^','~'],0],
  ['B','C Programming','What is the output of: printf("%d", (int)3.9);',['3','4','3.9','Error'],0],
  ['B','Data Structures','Which data structure uses LIFO principle?',['Queue','Stack','Array','Linked List'],1],
  ['B','Data Structures','What is the time complexity of binary search?',['O(n)','O(log n)','O(n log n)','O(1)'],1],
  ['B','Data Structures','A full binary tree with n leaves has how many internal nodes?',['n','n-1','n+1','2n'],1],
  ['B','Data Structures','Which traversal of a BST gives elements in sorted order?',['Preorder','Postorder','Inorder','Level order'],2],
  ['B','Data Structures','Time complexity of inserting an element at the beginning of a singly linked list?',['O(1)','O(n)','O(log n)','O(n²)'],0],
  ['B','Data Structures','Which data structure is used for BFS of a graph?',['Stack','Queue','Priority Queue','Array'],1],
  ['B','Data Structures','What is the average-case time complexity of quicksort?',['O(n²)','O(n log n)','O(n)','O(log n)'],1],
  ['B','Data Structures','In a circular queue with size 5, if front=2 and rear=4, how many elements are present?',['2','3','4','5'],1],
  ['B','OOP in C++','Which concept of OOP wraps data and functions together?',['Inheritance','Polymorphism','Encapsulation','Abstraction'],2],
  ['B','OOP in C++','What is the default access specifier for members of a class in C++?',['public','protected','private','none'],2],
  ['B','OOP in C++','Which function is automatically called when an object is created?',['Destructor','Constructor','main()','init()'],1],
  ['B','OOP in C++','What does the keyword "virtual" enable in C++?',['Compile-time polymorphism','Runtime polymorphism','Encapsulation','Data hiding'],1],
  ['B','OOP in C++','Which type of inheritance acquires features from more than one base class?',['Single','Multi-level','Multiple','Hierarchical'],2],
  ['B','OOP in C++','Which operator cannot be overloaded in C++?',['+ operator',':: (scope resolution)','<< operator','== operator'],1],
  ['B','OOP in C++','What is a template in C++?',['A blueprint for creating generic classes/functions','A type of constructor','A virtual function','An access specifier'],0],
  ['B','OOP in C++','Destructor in C++ has which of the following features?',['Can be overloaded','Returns a value','Has no parameters and cannot be overloaded','Is called explicitly only'],2],
  ['B','Operating Systems','Which scheduling algorithm may cause starvation?',['Round Robin','FCFS','Priority Scheduling','SJF (non-preemptive)'],2],
  ['B','Operating Systems','Deadlock cannot occur if which condition is prevented?',['Mutual Exclusion','Hold and Wait','No Preemption','Any one of the above'],3],
  ['B','Operating Systems','In paging, internal fragmentation occurs because:',['Pages are of variable size','The last page may not be fully used','Segments overlap','Page table is too large'],1],
  ['B','Operating Systems','What does a semaphore with initial value 1 act as?',['Counting semaphore','Binary semaphore / Mutex','Spinlock','Monitor'],1],
  ['B','Operating Systems','Which IPC mechanism allows processes to share memory directly?',['Pipes','Message Queues','Shared Memory','Sockets'],2],
  ['B','Operating Systems','Which file system is natively used by Linux?',['FAT32','NTFS','ext4','HFS+'],2],
  ['B','Operating Systems','The process state that indicates waiting for I/O completion is:',['Running','Ready','Blocked/Waiting','Terminated'],2],
  ['B','Networking','How many layers are in the OSI model?',['4','5','7','6'],2],
  ['B','Networking','Which protocol is used to assign IP addresses automatically?',['DNS','FTP','DHCP','HTTP'],2],
  ['B','Networking','What is the default subnet mask for a Class C IP address?',['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.128'],2],
  ['B','Networking','Which layer of OSI is responsible for end-to-end communication?',['Network','Data Link','Transport','Session'],2],
  ['B','Networking','What does DNS stand for and what does it do?',['Domain Name System – maps domain names to IP addresses','Data Network Service – encrypts data','Dynamic Name Server – assigns MAC addresses','Direct Network System – routes packets'],0],
  ['B','Big Data & AI Basics','What does Hadoop HDFS stand for?',['Hadoop Distributed File System','High Definition File Storage','Hierarchical Data Filing System','Hadoop Data Formatting Standard'],0],
  ['B','Big Data & AI Basics','MapReduce is a programming model used for:',['Web development','Processing large datasets in parallel across a cluster','Real-time database transactions','Mobile app development'],1],
  ['B','Big Data & AI Basics','Which of the following is a NoSQL database?',['MySQL','Oracle','MongoDB','PostgreSQL'],2],
  ['B','Big Data & AI Basics','Which type of machine learning uses labelled training data?',['Unsupervised Learning','Reinforcement Learning','Supervised Learning','Self-supervised Learning'],2],
  ['B','Big Data & AI Basics','Artificial Intelligence (AI) can best be described as:',['A database management system','The simulation of human intelligence processes by machines','A programming language','A type of computer hardware'],1],
  ['B','Big Data & AI Basics','Which of the following is an example of a Big Data processing framework?',['MS Excel','Apache Hadoop','Oracle Forms','Adobe Photoshop'],1],
  ['B','Big Data & AI Basics','A neural network is inspired by:',['A social network','The structure of the human brain','A relational database','A computer motherboard'],1],
]

# ================================================================
#  SET 2 — Advanced (100 questions)
# ================================================================
s2_data = [
  ['A','English – Vocabulary','Choose the SYNONYM of LACONIC',['Verbose','Brief','Eloquent','Detailed'],1],
  ['A','English – Vocabulary','Choose the ANTONYM of FRUGAL',['Thrifty','Wasteful','Economical','Careful'],1],
  ['A','English – Vocabulary','Choose the SYNONYM of TACITURN',['Talkative','Reserved','Cheerful','Angry'],1],
  ['A','English – Vocabulary','Choose the ANTONYM of DEARTH',['Scarcity','Lack','Abundance','Poverty'],2],
  ['A','English – Vocabulary','Choose the SYNONYM of EPHEMERAL',['Permanent','Transient','Eternal','Lasting'],1],
  ['A','English – Grammar','Fill in the blank: By the time he arrived, she ______ already left.',['has','had','have','was'],1],
  ['A','English – Grammar','Spot the error: "The news are very disturbing."',['The','news','are','disturbing'],2],
  ['A','English – Grammar','Fill in the blank: ______ of the two candidates is suitable for this post.',['Either','Neither','Both','None'],1],
  ['A','English – Grammar','Choose the correct sentence:',['He is one of those men who is honest.','He is one of those men who are honest.','He is one of the men who was honest.','He is one of those mens who are honest.'],1],
  ['A','English – Grammar','Fill in the blank: The jury ______ divided in its opinion.',['were','are','was','is being'],2],
  ['A','English – Reading Comprehension','Read the following passage:\n\nNeural networks are computational models inspired by the human brain, consisting of layers of interconnected nodes called neurons. Deep learning refers to neural networks with many layers, enabling them to learn complex representations of data. The training process involves feeding data forward through the network, computing a loss function, and then backpropagating errors to update weights using gradient descent. Convolutional Neural Networks (CNNs) excel at image recognition tasks, while Recurrent Neural Networks (RNNs) handle sequential data like text and speech. Deep learning has revolutionized fields including computer vision, natural language processing, and autonomous driving.\n\nWhat does "deep" in deep learning refer to?',['The complexity of data','Many layers in the neural network','The depth of datasets','The depth of the loss function'],1],
  ['A','English – Reading Comprehension','According to the passage, which network is best suited for image recognition?',['RNN','ANN','CNN','GAN'],2],
  ['A','English – Reading Comprehension','What is backpropagation used for in neural networks?',['Forward pass of data','Updating network weights based on errors','Initializing neuron values','Selecting the activation function'],1],
  ['A','English – Reading Comprehension','Which of the following fields has NOT been mentioned in the passage as being revolutionized by deep learning?',['Computer vision','Autonomous driving','Quantum computing','Natural language processing'],2],
  ['A','English – Reading Comprehension','Which algorithm is mentioned for updating weights during training?',['Backpropagation only','Gradient descent','Adam optimizer','Random search'],1],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: A place where animals are kept',['Aquarium','Aviary','Zoo','Sanctuary'],2],
  ['A','English – Para-jumble & One-word Substitution','Arrange:\nP: He was rushed to hospital.\nQ: The accident happened suddenly.\nR: Doctors operated immediately.\nS: He recovered in a week.',['QPRS','PQRS','RSPQ','SQRP'],0],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: A person who does not believe in God',['Agnostic','Atheist','Theist','Deist'],1],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: Government by the people',['Autocracy','Monarchy','Democracy','Oligarchy'],2],
  ['A','English – Para-jumble & One-word Substitution','Arrange:\nP: She submitted the project.\nQ: She worked late every night.\nR: Her professor was impressed.\nS: She started researching the topic.',['SQPR','PQSR','RSPQ','SQRP'],0],
  ['A','Quantitative Aptitude','Pipe A fills a tank in 12 hours, pipe B empties it in 18 hours. If both are open, when will the tank be full?',['36 hours','24 hours','30 hours','18 hours'],0],
  ['A','Quantitative Aptitude','A boat goes 24 km upstream in 6 hours and 20 km downstream in 4 hours. Find the speed of the stream.',['1 km/h','2 km/h','3 km/h','4 km/h'],0],
  ['A','Quantitative Aptitude','Find CI on Rs.8000 at 5% p.a. compounded half-yearly for 1 year.',['Rs.404','Rs.400','Rs.408.10','Rs.412'],2],
  ['A','Quantitative Aptitude','A sum doubles in 8 years at SI. What is the rate of interest?',['10%','12.5%','8%','15%'],1],
  ['A','Quantitative Aptitude','In a mixture of 80L, alcohol and water are in ratio 3:1. How much water must be added to make ratio 3:2?',['20L','16L','10L','18L'],1],
  ['A','Quantitative Aptitude','A train 200m long crosses a bridge 300m long at 72 km/h. Time taken?',['15 sec','20 sec','25 sec','30 sec'],2],
  ['A','Quantitative Aptitude','A and B can finish work in 18 days, B and C in 24 days, A and C in 36 days. In how many days can all three finish?',['16','18','20','24'],0],
  ['A','Quantitative Aptitude','Rs.1200 is divided among A, B, C in ratio 1:2:3. What is B\'s share?',['Rs.200','Rs.400','Rs.600','Rs.300'],1],
  ['A','Quantitative Aptitude','A sold an article at 20% loss. Had he sold it for Rs.200 more, he would have made 5% profit. Find cost price.',['Rs.600','Rs.700','Rs.800','Rs.1000'],2],
  ['A','Quantitative Aptitude','If 40% of a number is 120, what is 60% of that number?',['180','160','200','240'],0],
  ['A','Quantitative Aptitude','In how many ways can the letters of EXAM be arranged?',['12','24','18','6'],1],
  ['A','Quantitative Aptitude','What is the probability of drawing a red face card from a standard deck?',['3/26','1/13','3/52','1/4'],0],
  ['A','Quantitative Aptitude','A man is 3 times as old as his son. After 10 years, he will be twice as old. Find the son\'s current age.',['5','8','10','12'],2],
  ['A','Quantitative Aptitude','SI on a sum for 5 years at 6% p.a. is Rs.1500. Find the principal.',['Rs.4000','Rs.5000','Rs.6000','Rs.3000'],1],
  ['A','Quantitative Aptitude','Two numbers are in ratio 4:7. Their LCM is 168. Find the smaller number.',['24','28','32','42'],0],
  ['A','Reasoning','Find the missing term: 2, 3, 5, 8, 13, 21, ?',['30','34','35','32'],1],
  ['A','Reasoning','Find the next: Z, X, V, T, R, ?',['P','O','Q','S'],0],
  ['A','Reasoning','If HOSPITAL is coded by swapping each pair of adjacent letters, what is the coded form?',['OHSPTIAL','HOSITAPL','OHSITAPL','HSOIATLP'],1],
  ['A','Reasoning','Pointing to a woman, Ram says, "Her mother is the only daughter of my mother." How is Ram related to the woman?',['Brother','Father','Uncle','Son'],1],
  ['A','Reasoning','A man walks 10 km East, then 5 km South, then 10 km West. How far is he from start and in what direction?',['5 km North','5 km South','10 km South','5 km East'],1],
  ['A','Reasoning','Statements: All dogs are animals. No animal is a plant. Conclusions: I. No dog is a plant. II. Some plants are animals.',['Only I','Only II','Both','Neither'],0],
  ['A','Reasoning','Odd one out: 36, 49, 64, 81, 100, 111',['64','81','100','111'],3],
  ['A','Reasoning','A is B\'s sister. B is C\'s brother. C is D\'s son. D is E\'s wife. How is A related to E?',['Granddaughter','Daughter','Niece','Daughter-in-law'],0],
  ['A','Reasoning','What is the angle between clock hands at 6:30?',['0°','15°','3°','5°'],1],
  ['A','Reasoning','Find next: 1, 8, 27, 64, 125, ?',['196','216','256','169'],1],
  ['A','Reasoning','ACEG : BDFH :: IKMO : ?',['JLNP','KLNP','JLMP','ILNP'],0],
  ['A','Reasoning','In a class of 40, Anil ranks 12th from top and Bina ranks 15th from bottom. How many students are between them?',['13','14','15','16'],1],
  ['A','Reasoning','Find the missing number in: 5, 11, 23, 47, 95, ?',['190','191','192','193'],1],
  ['A','Reasoning','A is 40m East of B. C is 30m South of A. What is the shortest distance between B and C?',['50m','40m','60m','70m'],0],
  ['A','Reasoning','A is elder than B but younger than C. D is younger than B. Who is the youngest?',['A','B','C','D'],3],
  ['B','Computer Fundamentals','Convert decimal 255 to hexadecimal.',['EF','FE','FF','F0'],2],
  ['B','Computer Fundamentals','What is the output of XOR gate when inputs are A=1, B=1?',['0','1','Undefined','Both 0 and 1'],0],
  ['B','Computer Fundamentals','The 1\'s complement of 10110011 is:',['01001100','01001101','10110011','11001100'],0],
  ['B','Computer Fundamentals','The Boolean expression A.(A+B) simplifies to:',['A+B','A','B','AB'],1],
  ['B','Computer Fundamentals','Minimum number of NAND gates needed to implement NOT gate:',['1','2','3','4'],0],
  ['B','C Programming','What is the output?\n#include<stdio.h>\nint main(){\n  int x=10;\n  int *p=&x;\n  printf("%d", *p+2);\n  return 0;\n}',['10','12','2','Address'],1],
  ['B','C Programming','What is the output?\n#define MAX(a,b) ((a)>(b)?(a):(b))\nint main(){\n  int x=5,y=10;\n  printf("%d",MAX(x++,y++));\n  return 0;\n}',['10','11','5','6'],1],
  ['B','C Programming','What is the output?\nint i=0;\nwhile(i++<3)\n  printf("%d ",i);\n',['0 1 2 ','1 2 3 ','0 1 2 3 ','1 2 3 4'],1],
  ['B','C Programming','What is the output?\nint a[]={10,20,30};\nint *p=a;\np++;\nprintf("%d",*p);',['10','20','30','Garbage'],1],
  ['B','C Programming','What is the output?\nvoid f(int *x){ *x=*x+10; }\nmain(){ int a=5; f(&a); printf("%d",a); }',['5','10','15','Error'],2],
  ['B','C Programming','What is undefined behaviour in C?',['Accessing array within bounds','Dereferencing a NULL pointer','Using printf with %d for int','Declaring a variable'],1],
  ['B','C Programming','What is the output?\nprintf("%d", sizeof("hello"));',['5','6','4','8'],1],
  ['B','C Programming','What is the output?\nint x=7;\nprintf("%d %d", x>>1, x<<1);',['3 14','4 14','3 16','4 16'],0],
  ['B','C Programming','Which of the following correctly declares a pointer to a function returning int?',['int *f()','int (*f)()','int &f()','*int f()'],1],
  ['B','C Programming','What is the output?\nstatic int x=5;\nvoid f(){x++;}\nmain(){f();f();printf("%d",x);}',['5','6','7','Error'],2],
  ['B','Data Structures','What is the worst-case time complexity of AVL tree insertion?',['O(n)','O(log n)','O(n log n)','O(1)'],1],
  ['B','Data Structures','In a B-tree of order m, each internal node has at most how many children?',['m-1','m','m+1','2m'],1],
  ['B','Data Structures','What is the time complexity of DFS on a graph with V vertices and E edges?',['O(V)','O(E)','O(V+E)','O(V*E)'],2],
  ['B','Data Structures','Which dynamic programming algorithm finds shortest paths between all pairs of vertices?',['Dijkstra','Bellman-Ford','Floyd-Warshall','Prim\'s'],2],
  ['B','Data Structures','In hashing, the technique of using a second hash function to resolve collision is called:',['Linear Probing','Chaining','Quadratic Probing','Double Hashing'],3],
  ['B','Data Structures','What is the space complexity of merge sort?',['O(1)','O(log n)','O(n)','O(n log n)'],2],
  ['B','Data Structures','Postfix expression for A+B*C-D is:',['ABC*+D-','AB+C*D-','ABCD*+-','ABC+*D-'],0],
  ['B','Data Structures','Which of the following sorting algorithms is stable?',['Quick Sort','Heap Sort','Merge Sort','Shell Sort'],2],
  ['B','OOP in C++','Which feature of C++ allows the same function name with different parameters?',['Inheritance','Encapsulation','Function Overloading','Abstraction'],2],
  ['B','OOP in C++','What is a pure virtual function in C++?',['A function with no body','Declared as virtual int f() = 0;','A static member function','A friend function'],1],
  ['B','OOP in C++','In which inheritance type does the diamond problem occur?',['Single','Multi-level','Multiple','Hierarchical'],2],
  ['B','OOP in C++','What is a copy constructor used for?',['Creating object from another object of same class','Destroying an object','Overloading operators','Accessing private members'],0],
  ['B','OOP in C++','Which keyword is used to prevent a class from being inherited in modern C++?',['static','const','final','sealed'],2],
  ['B','OOP in C++','What does "this" pointer refer to in C++?',['Base class','Derived class','Current object','Parent function'],2],
  ['B','OOP in C++','Which of the following cannot be virtual in C++?',['Member function','Destructor','Constructor','Friend function'],2],
  ['B','OOP in C++','What is the difference between struct and class in C++?',['No difference','struct members are public by default; class members are private','class supports inheritance, struct does not','struct has no constructors'],1],
  ['B','Operating Systems','In Banker\'s algorithm, a state is safe if:',['All processes can get their maximum resources','No deadlock exists currently','There exists a sequence in which all processes can finish','Resources are equally distributed'],2],
  ['B','Operating Systems','Which page replacement algorithm suffers from Belady\'s anomaly?',['LRU','Optimal','FIFO','Clock'],2],
  ['B','Operating Systems','Thrashing occurs when:',['CPU utilization is very high','Processes spend more time paging than executing','There is too much free memory','The disk is full'],1],
  ['B','Operating Systems','Which scheduling algorithm gives minimum average waiting time for a given set of processes?',['FCFS','Round Robin','SJF','Priority'],2],
  ['B','Operating Systems','The optimal page replacement algorithm replaces:',['The least recently used page','The page that will not be used for the longest time in future','A random page','The most recently used page'],1],
  ['B','Operating Systems','In the Banker\'s algorithm, the Need matrix is computed as:',['Max – Allocated','Allocated – Max','Max + Allocated','Available – Allocated'],0],
  ['B','Operating Systems','What is a critical section?',['A section of code accessing shared resources','A section causing deadlock','The kernel space of memory','A CPU register'],0],
  ['B','Networking','What is the purpose of the ARP protocol?',['Assign IP addresses dynamically','Map IP addresses to MAC addresses','Encrypt network traffic','Route packets between networks'],1],
  ['B','Networking','Which layer of OSI model does IP operate at?',['Transport','Data Link','Network','Session'],2],
  ['B','Networking','The maximum number of usable hosts in a /26 subnet is:',['30','62','126','254'],1],
  ['B','Networking','Which protocol provides reliable, connection-oriented communication?',['UDP','IP','TCP','ICMP'],2],
  ['B','Networking','The HTTP status code 404 means:',['Server Error','Unauthorized','Not Found','Redirect'],2],
  ['B','Big Data & AI Basics','What is the default block size in HDFS (Hadoop 2.x and later)?',['32 MB','64 MB','128 MB','256 MB'],2],
  ['B','Big Data & AI Basics','Apache Spark\'s main advantage over Hadoop MapReduce is:',['Better security','In-memory processing, making it significantly faster','Cheaper hardware requirements','Better SQL support only'],1],
  ['B','Big Data & AI Basics','What does the term "3 Vs of Big Data" refer to?',['Volume, Velocity, Variety','Vision, Value, Velocity','Volume, Value, Validity','Variety, Validity, Velocity'],0],
  ['B','Big Data & AI Basics','Which of the following best describes Machine Learning?',['Manually coding rules for every decision','A system that explicitly learns patterns from data to make predictions','A type of database query language','A computer network protocol'],1],
  ['B','Big Data & AI Basics','Overfitting in a machine learning model means:',['The model performs poorly on training data','The model performs well on training but poorly on unseen data','The model has too few parameters','The training data is too large'],1],
  ['B','Big Data & AI Basics','Which algorithm is commonly used for classification and regression in ML?',['PageRank','Decision Tree','SHA-256','Bubble Sort'],1],
  ['B','Big Data & AI Basics','What is a neural network inspired by?',['Computer circuits','The structure of the human brain','Social networks','Database tables'],1],
]

# ================================================================
#  SET 3 — Advanced + Section C (150 questions)
# ================================================================
s3_data = [
  # --- Section A (50) ---
  ['A','English – Vocabulary','Choose the SYNONYM of AUSPICIOUS',['Unfavorable','Promising','Gloomy','Harsh'],1],
  ['A','English – Vocabulary','Choose the ANTONYM of CANDID',['Frank','Secretive','Open','Direct'],1],
  ['A','English – Vocabulary','Choose the SYNONYM of TENACIOUS',['Yielding','Persistent','Flexible','Fragile'],1],
  ['A','English – Vocabulary','Choose the ANTONYM of MAGNANIMOUS',['Generous','Noble','Petty','Grand'],2],
  ['A','English – Vocabulary','Choose the SYNONYM of IMPETUOUS',['Calm','Cautious','Rash','Thoughtful'],2],
  ['A','English – Grammar','Fill in the blank: The teacher along with her students ______ to the museum.',['go','have gone','goes','were going'],2],
  ['A','English – Grammar','Spot the error: "He is a man of principles and who works hard."',['He is','a man of principles','and who','works hard'],2],
  ['A','English – Grammar','Fill in the blank: No sooner did she see the snake ______ she screamed.',['then','than','when','that'],1],
  ['A','English – Grammar','Which sentence uses the subjunctive mood correctly?',['If I was you, I would stop.','If I were you, I would stop.','If I am you, I would stop.','If I be you, I would stop.'],1],
  ['A','English – Grammar','Fill in the blank: She insisted that he ______ present at the meeting.',['is','was','be','were'],2],
  ['A','English – Reading Comprehension','Read the following passage:\n\nArtificial Intelligence (AI) and Machine Learning (ML) are increasingly embedded in systems that affect human lives — from loan approvals and hiring decisions to criminal sentencing and medical diagnoses. This raises profound ethical questions. Algorithmic bias, where AI systems reproduce or amplify societal prejudices, is a major concern. For example, facial recognition systems have been found to be less accurate for darker-skinned individuals. Transparency and explainability — the ability to understand why an AI makes a decision — are critical for accountability. Regulatory frameworks like the EU AI Act aim to classify AI systems by risk level and impose obligations accordingly. Ethics in AI is not just a technical challenge but a socio-political one.\n\nWhat is the primary concern about AI described in the passage?',['Speed of computation','Algorithmic bias and ethical issues','Cost of development','Hardware limitations'],1],
  ['A','English – Reading Comprehension','What example of algorithmic bias is given in the passage?',['Loan approval errors','Biased criminal sentencing','Less accurate facial recognition for darker-skinned individuals','Hiring discrimination against women'],2],
  ['A','English – Reading Comprehension','What does the EU AI Act aim to do, according to the passage?',['Ban all AI systems','Classify AI by risk level and impose obligations','Promote AI development without restrictions','Provide AI funding to startups'],1],
  ['A','English – Reading Comprehension','What does "explainability" mean in the context of AI ethics in the passage?',['Making AI faster','Understanding why an AI makes a decision','Reducing AI costs','Training AI on more data'],1],
  ['A','English – Reading Comprehension','According to the passage, ethics in AI is:',['Purely a technical challenge','Only a political issue','Both a technical and socio-political challenge','A hardware problem'],2],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: Fear of open or public places',['Claustrophobia','Agoraphobia','Xenophobia','Hydrophobia'],1],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: One who feeds on flesh',['Herbivore','Omnivore','Carnivore','Insectivore'],2],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: A medicine that kills bacteria',['Antidote','Antibiotic','Antiseptic','Vaccine'],1],
  ['A','English – Para-jumble & One-word Substitution','Arrange:\nP: The scientist announced the discovery.\nQ: Years of research had preceded this moment.\nR: The world was astonished.\nS: It would change medicine forever.',['QPRS','PQSR','RSPQ','SQRP'],0],
  ['A','English – Para-jumble & One-word Substitution','One word substitution: A speech made without preparation',['Extempore','Soliloquy','Monologue','Oration'],0],
  ['A','Quantitative Aptitude','Find the sum of first 20 natural numbers.',['200','210','190','220'],1],
  ['A','Quantitative Aptitude','A train 300m long running at 90 km/h crosses another train 200m long running at 54 km/h in opposite directions. Time taken?',['10 sec','15 sec','20 sec','25 sec'],0],
  ['A','Quantitative Aptitude','If 5 men can do a work in 8 days, how many men are needed to complete it in 4 days?',['8','10','12','15'],1],
  ['A','Quantitative Aptitude','A mixture of 100L contains milk and water in ratio 7:3. How much mixture must be removed and replaced with water to make ratio 3:7?',['40L','57.14L','50L','66.67L'],1],
  ['A','Quantitative Aptitude','Find the compound interest on Rs.15000 at 8% p.a. for 3 years (approximate).',['Rs.3779.52','Rs.3600','Rs.4000','Rs.3600.00'],0],
  ['A','Quantitative Aptitude','A can do 1/3 of a work in 5 days, B can do 2/5 of the work in 10 days. In how many days will both finish the work together?',['75/8 days','8.5 days','9 days','10 days'],0],
  ['A','Quantitative Aptitude','Two trains start simultaneously from stations A and B, 300 km apart, towards each other at 70 and 80 km/h. When do they meet?',['2 hrs','1.5 hrs','2.5 hrs','3 hrs'],0],
  ['A','Quantitative Aptitude','If the digits of a two-digit number are reversed, the new number is 18 more than the original. The sum of digits is 10. Find the original number.',['46','37','64','73'],0],
  ['A','Quantitative Aptitude','Find the number of ways to select a committee of 3 from 8 people.',['56','24','336','120'],0],
  ['A','Quantitative Aptitude','The difference between CI and SI on Rs.1600 at 5% p.a. for 2 years is:',['Rs.4','Rs.8','Rs.16','Rs.20'],0],
  ['A','Quantitative Aptitude','A shopkeeper gives 20% discount on MRP and still makes 20% profit. If MRP is Rs.600, find the cost price.',['Rs.400','Rs.450','Rs.500','Rs.480'],0],
  ['A','Quantitative Aptitude','A person rows 30 km downstream in 5 hours and 18 km upstream in 6 hours. Find the speed of the current.',['1 km/h','2 km/h','1.5 km/h','0.5 km/h'],2],
  ['A','Quantitative Aptitude','What is the probability that a card drawn from a deck is a King or a Heart?',['4/13','17/52','5/13','16/52'],1],
  ['A','Quantitative Aptitude','Find the HCF of 144, 180, and 252.',['12','18','36','9'],2],
  ['A','Quantitative Aptitude','A and B invest Rs.3000 and Rs.4000 in a business. A receives 10% of profit as salary and rest is shared proportionally. If total profit is Rs.3500, find A\'s total earnings.',['Rs.1500','Rs.1850','Rs.1800','Rs.2000'],1],
  ['A','Reasoning','Find the odd one out: Mercury, Venus, Earth, Sun, Mars',['Mercury','Venus','Sun','Mars'],2],
  ['A','Reasoning','Find the next term: 3, 6, 11, 18, 27, ?',['36','38','40','42'],1],
  ['A','Reasoning','If all Bloops are Razzies and all Razzies are Lazzies, then:',['All Bloops are Lazzies','All Lazzies are Bloops','Some Lazzies are Bloops','None of the above'],0],
  ['A','Reasoning','Find next in series: B2, D4, F8, H16, ?',['J32','I32','J24','K32'],0],
  ['A','Reasoning','In a row of 25, if Tom is 10th from left and Jerry is 12th from right, how many are between them?',['3','4','5','6'],0],
  ['A','Reasoning','How many times do the hands of a clock coincide in 24 hours?',['22','24','44','48'],2],
  ['A','Reasoning','In a group, A is the husband of B. C is the son of A. D is the brother of C. E is the mother of D. How is E related to B?',['Daughter','Daughter-in-law','They are the same person','Sister'],2],
  ['A','Reasoning','In a certain language, ROPE is coded as SPQF. How is LAKE coded?',['MBLF','MBKF','MALF','KBJD'],0],
  ['A','Reasoning','Find missing number in series: 4, 9, 25, 49, 121, ?, 169',['144','196','100','225'],2],
  ['A','Reasoning','Statements: Some cats are dogs. All dogs are horses. Conclusion: Some cats are horses.',['True','False','Cannot be determined','Insufficient data'],0],
  ['A','Reasoning','A clock was set right at 8 AM. It gains 10 minutes in 24 hours. What will it show at 8 PM of the same day?',['8:05 PM','8:10 PM','8:04 PM','8:05:30 PM'],0],
  ['A','Reasoning','Find the next term in series: 144, 121, 100, 81, 64, ?',['49','36','25','16'],0],
  ['A','Reasoning','If ABCD = 1234 and EFGH = 5678, what is BFHD?',['2678','2658','2648','2578'],0],
  ['A','Reasoning','Rohit is taller than Suresh but shorter than Amit. Priya is taller than Rohit. Who is the shortest?',['Rohit','Suresh','Priya','Amit'],1],
  ['A','Reasoning','In a code: MONKEY = XDJMNL, how is TIGER coded?',['QDFHS','SHFDQ','QHFDS','OFDHS'],0],
  # --- Section B (50) ---
  ['B','Computer Fundamentals','What is the decimal equivalent of binary 111111?',['63','64','62','127'],0],
  ['B','Computer Fundamentals','Convert hexadecimal 1A3 to decimal.',['419','421','423','415'],0],
  ['B','Computer Fundamentals','The minimum number of NOR gates to implement a NOT gate is:',['1','2','3','4'],0],
  ['B','Computer Fundamentals','The result of 1011 AND 1101 in binary is:',['1001','1010','1111','0110'],0],
  ['B','Computer Fundamentals','De Morgan\'s theorem states that (AB)\' = ?',["A' + B'","A'B'",'A + B','AB'],0],
  ['B','C Programming','What is the output?\n#include<stdio.h>\nint main(){\n  int i=1;\n  printf("%d %d %d", i, i++, ++i);\n  return 0;\n}',['1 1 3','3 2 3','Undefined Behaviour','1 2 3'],2],
  ['B','C Programming','What is the output?\nvoid f(int a[]){\n  a[0]=100;\n}\nmain(){\n  int arr[]={1,2,3};\n  f(arr);\n  printf("%d",arr[0]);\n}',['1','100','Error','Garbage'],1],
  ['B','C Programming','What does the following macro do?\n#define SWAP(a,b) {int t=a; a=b; b=t;}',['Swaps two variables using a macro','Swaps two pointers','Causes undefined behaviour','Fails to compile'],0],
  ['B','C Programming','What is the output?\nint x=5;\nprintf("%d", x<<2);',['10','15','20','25'],2],
  ['B','C Programming','What is the output?\nchar *p="Hello";\np[0]=\'h\';\nprintf("%s",p);',['Hello','hello','Undefined Behaviour / Segfault','Error'],2],
  ['B','C Programming','What is the output?\nint a=10,b=5;\nprintf("%d",a^b);',['5','10','15','3'],2],
  ['B','C Programming','How many bytes does int arr[5] occupy on a 32-bit system?',['5','10','20','40'],2],
  ['B','C Programming','What is the output?\nvoid fun(int *ptr){\n  ptr=ptr+1;\n}\nmain(){\n  int a=10;\n  fun(&a);\n  printf("%d",a);\n}',['10','11','Garbage','Error'],0],
  ['B','C Programming','Which function is used to dynamically allocate memory and initialize it to zero?',['malloc','calloc','realloc','alloc'],1],
  ['B','C Programming','What is the output?\nint x=10;\nif(x=0)\n  printf("Zero");\nelse\n  printf("Non-zero");',['Zero','Non-zero','Error','Undefined'],1],
  ['B','Data Structures','What is the time complexity of finding the kth smallest element in a balanced BST?',['O(1)','O(k)','O(log n)','O(n)'],1],
  ['B','Data Structures','In an AVL tree, the balance factor of a node can be:',['−2, −1, 0, 1, 2','−1, 0, 1','0, 1','−1, 0'],1],
  ['B','Data Structures','Which of the following is NOT a property of a B+ tree?',['All data is stored in leaf nodes','Leaf nodes are linked','Internal nodes store only keys','Root can have only one child'],3],
  ['B','Data Structures','What is the time complexity of Bellman-Ford algorithm?',['O(V+E)','O(V*E)','O(V^2)','O(E log V)'],1],
  ['B','Data Structures','In dynamic programming, overlapping subproblems means:',['Subproblems share no solutions','Same subproblems are solved multiple times','Each subproblem is unique','Problems cannot be divided'],1],
  ['B','Data Structures','What is the worst-case time complexity of heapsort?',['O(n^2)','O(n log n)','O(n)','O(log n)'],1],
  ['B','Data Structures','The number of edges in a complete graph of n vertices is:',['n(n-1)','n(n-1)/2','n^2','n(n+1)/2'],1],
  ['B','Data Structures','Which of the following sorting algorithms is NOT comparison-based?',['Merge Sort','Quick Sort','Counting Sort','Heap Sort'],2],
  ['B','OOP in C++','What is the output?\nclass A{\npublic:\n  A(){cout<<"A";}\n  ~A(){cout<<"~A";}\n};\nint main(){\n  A obj;\n  return 0;\n}',['A','~A','A~A','Error'],2],
  ['B','OOP in C++','Which type of polymorphism is resolved at compile time?',['Runtime polymorphism','Dynamic binding','Compile-time polymorphism','Late binding'],2],
  ['B','OOP in C++','What is the purpose of a virtual destructor?',['To prevent object creation','To ensure derived class destructor is called via base pointer','To overload destructors','To make class abstract'],1],
  ['B','OOP in C++','Can constructors be virtual in C++?',['Yes','No','Only in abstract classes','Only with inheritance'],1],
  ['B','OOP in C++','What does the "friend" keyword do in C++?',['Makes a class inherit another','Grants external function access to private members','Creates a virtual function','Overloads operators'],1],
  ['B','OOP in C++','STL stands for:',['Standard Template Library','Static Type Library','System Template Library','Structured Type Library'],0],
  ['B','OOP in C++','Which concept does the following demonstrate?\nvoid draw(Shape *s) { s->render(); }',['Encapsulation','Runtime polymorphism','Compile-time polymorphism','Abstraction'],1],
  ['B','OOP in C++','What is the output of sizeof on a class with no data members?',['0','1','4','Compiler dependent'],1],
  ['B','Operating Systems','What is the purpose of the Translation Lookaside Buffer (TLB)?',['Store page tables','Speed up virtual-to-physical address translation','Cache disk data','Handle interrupts'],1],
  ['B','Operating Systems','What is the difference between paging and segmentation?',['Paging divides into fixed-size pages; segmentation into variable-size logical segments','Paging uses variable-size blocks; segmentation uses fixed','Both are the same','Segmentation is for virtual memory only'],0],
  ['B','Operating Systems','Which of the following conditions is NOT one of the four Coffman conditions for deadlock?',['Mutual Exclusion','Hold and Wait','Starvation','Circular Wait'],2],
  ['B','Operating Systems','In round-robin scheduling, what happens if a process needs burst time less than the time quantum?',['It waits for the full quantum','It releases CPU voluntarily when done','It is preempted after q time','It is sent to blocked state'],1],
  ['B','Operating Systems','What is the role of the page table in an OS?',['Store actual data pages','Map virtual addresses to physical addresses','Schedule processes','Manage disk I/O'],1],
  ['B','Operating Systems','Which system call is used to create a new process in UNIX/Linux?',['exec()','spawn()','fork()','create()'],2],
  ['B','Operating Systems','What is a race condition?',['Two processes running at same speed','Outcome depends on timing of concurrent operations','A process running faster than expected','An OS scheduling error'],1],
  ['B','Networking','What is the difference between TCP and UDP?',['TCP is connectionless, UDP is connection-oriented','TCP provides reliable delivery; UDP does not guarantee delivery','UDP is slower than TCP','TCP is used for streaming, UDP for web browsing'],1],
  ['B','Networking','Which protocol is used for secure web communication?',['HTTP','FTP','HTTPS/TLS','SMTP'],2],
  ['B','Networking','What is the size of an IPv6 address?',['32 bits','64 bits','128 bits','256 bits'],2],
  ['B','Networking','In a /28 subnet, how many usable host addresses are available?',['14','16','30','12'],0],
  ['B','Networking','Which device operates at the Network layer of OSI?',['Hub','Switch','Router','Bridge'],2],
  ['B','Big Data & AI Basics','In Hadoop, what is the role of YARN?',['Store data in HDFS','Provide SQL queries over Hadoop','Cluster resource management and job scheduling','Data replication across nodes'],2],
  ['B','Big Data & AI Basics','Spark RDD stands for:',['Reliable Distributed Dataset','Resilient Distributed Dataset','Replicated Data Directory','Remote Data Descriptor'],1],
  ['B','Big Data & AI Basics','Which of the following is a Spark transformation (not an action)?',['collect()','count()','map()','save()'],2],
  ['B','Big Data & AI Basics','The "bias-variance tradeoff" in machine learning refers to:',['A tradeoff between number of features and dataset size','The balance between underfitting (high bias) and overfitting (high variance)','A CPU vs memory optimization','A tradeoff between accuracy and training speed'],1],
  ['B','Big Data & AI Basics','K-Means clustering is an example of which type of learning?',['Supervised Learning','Unsupervised Learning','Reinforcement Learning','Semi-supervised Learning'],1],
  ['B','Big Data & AI Basics','Which metric is most appropriate for evaluating a classifier on an imbalanced dataset?',['Accuracy','Mean Squared Error','F1-Score','R-squared'],2],
  ['B','Big Data & AI Basics','TF-IDF in NLP stands for:',['Term Frequency-Inverse Document Frequency','Total Features-Integrated Data Format','Token Filter-Index Distance Function','Text Frequency-Inverse Density Factor'],0],
  # --- Section C (50) — Embedded Systems, Digital Electronics, Microprocessors ---
  # Digital Electronics (10)
  ['C','Digital Electronics','The output of a NAND gate is LOW only when:',['All inputs are LOW','Any input is HIGH','All inputs are HIGH','Any input is LOW'],2],
  ['C','Digital Electronics','Minimum number of 2-input NAND gates required to implement a 2-input AND gate:',['1','2','3','4'],1],
  ['C','Digital Electronics','The K-map of F = AB + A\'B simplifies to:',['A','B','A+B','AB'],1],
  ['C','Digital Electronics','A D flip-flop is used to:',['Amplify digital signals','Store 1 bit of data','Add two binary numbers','Multiply binary values'],1],
  ['C','Digital Electronics','A 4-to-1 multiplexer requires how many select lines?',['1','2','3','4'],1],
  ['C','Digital Electronics','XOR of any variable A with 1 gives:',["A","A'","0","1"],1],
  ['C','Digital Electronics','The Gray code representation of decimal 5 is:',['0101','0111','0110','1000'],1],
  ['C','Digital Electronics','An SR latch with S=1, R=1 results in:',['Set state','Reset state','No change','Forbidden/Invalid state'],3],
  ['C','Digital Electronics','A full adder accepts how many inputs?',['1','2','3','4'],2],
  ['C','Digital Electronics','Propagation delay in a logic gate refers to:',['Power consumed by the gate','Time for output to respond after input changes','Voltage level at output','Number of gates in series'],1],
  # 8085 Microprocessor (8)
  ['C','8085 Microprocessor','The 8085 microprocessor has a data bus width of:',['4 bits','8 bits','16 bits','32 bits'],1],
  ['C','8085 Microprocessor','Which instruction loads the accumulator directly from a memory address in 8085?',['MOV A,M','LDA addr','MVI A,data','IN port'],1],
  ['C','8085 Microprocessor','The program counter (PC) in 8085 is:',['8-bit register','12-bit register','16-bit register','32-bit register'],2],
  ['C','8085 Microprocessor','In 8085, the TRAP interrupt is:',['Maskable and edge-triggered','Non-maskable and highest priority vectored interrupt','Software interrupt only','Maskable and level-triggered'],1],
  ['C','8085 Microprocessor','The SID and SOD pins of 8085 are used for:',['Interrupt acknowledge','Serial data input/output','Status signals','Power supply'],1],
  ['C','8085 Microprocessor','8085 has how many general-purpose 8-bit registers?',['4','5','6','8'],2],
  ['C','8085 Microprocessor','In 8085, the instruction RNZ stands for:',['Return if Zero','Return if Not Zero','Reset if Non-Zero','Read Non-Zero'],1],
  ['C','8085 Microprocessor','The stack pointer (SP) in 8085 always points to:',['Bottom of the stack','Top of the stack (last pushed byte)','Next empty location in stack','Middle of the stack'],1],
  # 8086 Microprocessor (5)
  ['C','8086 Microprocessor','The 8086 microprocessor has an internal data bus width of:',['8 bits','12 bits','16 bits','32 bits'],2],
  ['C','8086 Microprocessor','Physical address in 8086 is calculated as:',['Segment + Offset','Segment × 16 + Offset','Segment × 8 + Offset','Segment × 4 + Offset'],1],
  ['C','8086 Microprocessor','How many segment registers does the 8086 have?',['2','3','4','6'],2],
  ['C','8086 Microprocessor','Which addressing mode in 8086 uses a base register plus a displacement?',['Immediate','Register','Based (Register Indirect with displacement)','Indexed'],2],
  ['C','8086 Microprocessor','The 8086 instruction set follows which architecture?',['RISC','CISC','VLIW','Harvard'],1],
  # Embedded C / Microcontrollers (8)
  ['C','Embedded C','The "volatile" keyword in embedded C tells the compiler:',['The variable is a constant','Do not optimize reads/writes; variable may change outside program control','The variable is in ROM','The variable is shared between functions'],1],
  ['C','Embedded C','GPIO stands for:',['General Purpose Input/Output','Global Process I/O','Graphical Processing Interface Output','Generic Peripheral I/O'],0],
  ['C','Embedded C','A watchdog timer in an embedded system is primarily used to:',['Measure elapsed time','Generate PWM signals','Reset the system if software hangs or enters an infinite loop','Synchronize serial communication'],2],
  ['C','Embedded C','PWM (Pulse Width Modulation) is commonly used to:',['Measure temperature','Control motor speed and LED brightness by varying duty cycle','Store data in EEPROM','Communicate over I2C'],1],
  ['C','Embedded C','To set bit 3 of variable x without affecting other bits, the correct C expression is:',['x = x | 3','x = x | (1 << 3)','x = x & (1 << 3)','x = x ^ 3'],1],
  ['C','Embedded C','To clear bit 5 of variable x without affecting other bits, use:',['x = x & ~(1 << 5)','x = x | (1 << 5)','x = x ^ (1 << 5)','x = x – (1 << 5)'],0],
  ['C','Embedded C','In embedded C, a memory-mapped register is typically declared as:',['int reg = 0x40020000;','#define REG 0x40020000','volatile uint32_t *reg = (volatile uint32_t*)0x40020000;','static int *reg;'],2],
  ['C','Embedded C','An ISR (Interrupt Service Routine) should generally:',['Perform lengthy computations','Be as short and fast as possible','Call blocking functions','Disable all interrupts permanently'],1],
  # RTOS (5)
  ['C','RTOS','RTOS stands for:',['Real-Time Operating System','Remote Terminal Operating System','Rapid Task Operating System','Run-Time Object System'],0],
  ['C','RTOS','In an RTOS, a task with higher priority:',['Always waits for lower-priority tasks','Preempts lower-priority tasks when it becomes ready','Shares equal time with all tasks','Cannot access shared resources'],1],
  ['C','RTOS','A mutex in RTOS is used to:',['Send messages between tasks','Provide mutual exclusion to protect shared resources','Create new tasks','Measure task execution time'],1],
  ['C','RTOS','Context switching in an RTOS refers to:',['Switching between different CPUs','Saving the state of the current task and restoring the state of the next task','Switching communication protocols','Changing the clock frequency'],1],
  ['C','RTOS','Which of the following is a symptom of priority inversion?',['High-priority task runs faster','High-priority task is blocked by a low-priority task holding a shared resource','All tasks run at equal priority','CPU becomes idle'],1],
  # ARM Architecture (5)
  ['C','ARM Architecture','ARM stands for:',['Automatic Register Machine','Advanced RISC Machine','Asynchronous RAM Module','Application Runtime Memory'],1],
  ['C','ARM Architecture','ARM processors are based on which ISA?',['CISC','RISC','VLIW','EPIC'],1],
  ['C','ARM Architecture','The Thumb instruction set on ARM uses:',['32-bit instructions only','16-bit compressed instructions for smaller code size','64-bit instructions','Variable-length instructions'],1],
  ['C','ARM Architecture','ARM Cortex-M series is primarily targeted for:',['Server computing','Microcontrollers and embedded systems','Desktop processors','GPU processing'],1],
  ['C','ARM Architecture','The LDR instruction in ARM assembly is used to:',['Store a register value to memory','Load a value from memory into a register','Perform logical AND','Branch to a subroutine'],1],
  # Serial Interfaces (5)
  ['C','Serial Interfaces','The I2C protocol uses how many signal wires (excluding power)?',['1','2','3','4'],1],
  ['C','Serial Interfaces','SPI (Serial Peripheral Interface) supports which communication mode?',['Half-duplex only','Asynchronous only','Full-duplex synchronous','Asynchronous serial'],2],
  ['C','Serial Interfaces','UART stands for:',['Universal Asynchronous Receiver-Transmitter','Unified Addressable Register Transfer','Universal Address Routing Table','Unified Asynchronous RAM Transfer'],0],
  ['C','Serial Interfaces','The CAN (Controller Area Network) bus is primarily used in:',['Consumer electronics','Automotive and industrial embedded systems','Wireless sensor networks','Cloud computing infrastructure'],1],
  ['C','Serial Interfaces','Which serial protocol uses a Master-Slave architecture with chip-select (CS) lines for each slave?',['I2C','UART','SPI','RS-232'],2],
  # IoT Basics (4)
  ['C','IoT Basics','An actuator in an IoT system is a device that:',['Senses physical parameters','Converts electrical signals into physical actions (motion, heat, light)','Stores sensor data','Provides wireless connectivity'],1],
  ['C','IoT Basics','MQTT protocol is best described as:',['A file transfer protocol','A lightweight publish-subscribe messaging protocol designed for IoT','A video streaming protocol','A database query language'],1],
  ['C','IoT Basics','OTA (Over-The-Air) update in embedded/IoT systems means:',['Updating firmware/software wirelessly without physical access to the device','Sending data over the air','Connecting sensors via Bluetooth','Broadcasting sensor data'],0],
  ['C','IoT Basics','Which of the following wireless protocols is most commonly used for short-range, low-power IoT communication?',['Wi-Fi 6','4G LTE','Zigbee / Bluetooth Low Energy (BLE)','Ethernet'],2],
]

# ================================================================
#  VERIFY COUNTS
# ================================================================
assert len(s1_data) == 100, f"Set 1 count wrong: {len(s1_data)}"
assert len(s2_data) == 100, f"Set 2 count wrong: {len(s2_data)}"
assert len(s3_data) == 150, f"Set 3 count wrong: {len(s3_data)}"
print(f"Question counts: Set1={len(s1_data)}, Set2={len(s2_data)}, Set3={len(s3_data)}")

# ================================================================
#  ENCODE ANSWER KEYS
# ================================================================
s1_ak = encode_ak([q[4] for q in s1_data])
s2_ak = encode_ak([q[4] for q in s2_data])
s3_ak = encode_ak([q[4] for q in s3_data])
print(f"AKs computed: s1={len(s1_ak)}, s2={len(s2_ak)}, s3={len(s3_ak)}")

# ================================================================
#  READ EXISTING HTML
# ================================================================
with open(HTML_PATH, 'r') as f:
    html = f.read()

# Extract Set 4 AK
# Try SETS structure first (already-transformed HTML), then old single-set format
set4_marker = "'4': { name:'Practice Set 4'"
if set4_marker in html:
    set4_start = html.index(set4_marker)
    ak4_match = re.search(r"ak:'([A-Za-z0-9+/=]+)'", html[set4_start:set4_start+300])
else:
    ak4_match = re.search(r"atob\('([A-Za-z0-9+/=]+)'\)", html)
if not ak4_match:
    print("ERROR: Could not find Set 4 AK in existing HTML")
    sys.exit(1)
s4_ak = ak4_match.group(1)

# Extract Set 4 questions using bracket depth counting to find the exact closing ]
if set4_marker in html:
    q_start = html.index('questions:[', html.index(set4_marker)) + len('questions:[')
    depth, i, in_str, esc, str_char = 1, q_start, False, False, None
    while i < len(html) and depth > 0:
        ch = html[i]
        if esc:
            esc = False
        elif ch == '\\' and in_str:
            esc = True
        elif in_str:
            if ch == str_char:
                in_str = False
        elif ch in ('"', "'"):
            in_str, str_char = True, ch
        elif ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
        i += 1
    q4_content = html[q_start:i-1]  # content between the outer [ and ]
else:
    q4_match = re.search(r'const Q = \[(.*?)\n\];', html, re.DOTALL)
    if not q4_match:
        print("ERROR: Could not find Set 4 Q array in existing HTML")
        sys.exit(1)
    q4_content = q4_match.group(1)
print(f"Set 4 extracted: Q array chars={len(q4_content)}, AK={s4_ak[:20]}...")

# Sanitize q4_content: replace any literal newlines inside JSON strings
# (these can be introduced if a previous generate run had the re.sub escaping bug)
def sanitize_js_strings(text):
    """Fix literal newlines inside JS string literals (both ' and " quoted)."""
    out, quote, esc = [], None, False
    for ch in text:
        if esc:
            out.append(ch); esc = False; continue
        if ch == '\\':
            out.append(ch); esc = True; continue
        if quote is None and ch in ('"', "'"):
            quote = ch; out.append(ch); continue
        if quote and ch == quote:
            quote = None; out.append(ch); continue
        if quote and ch == '\n':
            out.append('\\n'); continue
        if quote and ch == '\r':
            out.append('\\r'); continue
        out.append(ch)
    return ''.join(out)
q4_content = sanitize_js_strings(q4_content)

# ================================================================
#  BUILD QUESTION JS
# ================================================================
s1_qs = qs_to_js(s1_data)
s2_qs = qs_to_js(s2_data)
s3_qs = qs_to_js(s3_data)

# ================================================================
#  NEW CSS
# ================================================================
NEW_CSS = """
/* ===== SET SELECTOR ===== */
.set-cards-grid {
  display: grid; grid-template-columns: repeat(2, 1fr);
  gap: 14px; max-width: 660px; width: 100%; margin: 16px 0;
}
@media(max-width:540px){ .set-cards-grid { grid-template-columns: 1fr; } }
.set-card {
  background: rgba(255,255,255,0.12); border: 2px solid rgba(255,255,255,0.2);
  border-radius: 12px; padding: 16px 20px; cursor: pointer; position: relative;
  text-align: left; transition: all 0.15s;
}
.set-card:hover { background: rgba(255,255,255,0.22); border-color: rgba(255,255,255,0.5); transform: translateY(-2px); }
.set-card.selected { background: rgba(255,255,255,0.25); border-color: #fff; box-shadow: 0 0 0 3px rgba(255,255,255,0.3); }
.sc-num  { font-size: 0.73rem; opacity: 0.7; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 3px; }
.sc-name { font-size: 1rem; font-weight: 700; margin-bottom: 4px; }
.sc-meta { font-size: 0.76rem; opacity: 0.8; }
.sc-badge {
  position: absolute; top: 10px; right: 12px;
  font-size: 0.65rem; padding: 2px 9px; border-radius: 10px;
  font-weight: 700; letter-spacing: 0.5px; background: rgba(255,255,255,0.2);
}
.set-card.selected .sc-badge { background: #43a047; }
#set-info-panel { text-align: center; width: 100%; max-width: 660px; }
"""

# ================================================================
#  NEW WAITING SCREEN HTML
# ================================================================
NEW_WAITING = """<div id="waiting-screen">
  <h1>CDAC C-CAT Mock Test</h1>
  <div class="subtitle">Select a Practice Set to Begin</div>
  <div class="set-cards-grid">
    <div class="set-card" id="card-1" onclick="selectSet('1')">
      <div class="sc-badge">Normal</div>
      <div class="sc-num">Practice Set 1</div>
      <div class="sc-name">Section A + B</div>
      <div class="sc-meta">100 Questions &nbsp;&middot;&nbsp; 2 Hours</div>
      <div class="sc-meta" style="font-size:0.7rem;opacity:0.65;margin-top:3px;">English, Quant, Reasoning + CS Fundamentals</div>
    </div>
    <div class="set-card" id="card-2" onclick="selectSet('2')">
      <div class="sc-badge">Advanced</div>
      <div class="sc-num">Practice Set 2</div>
      <div class="sc-name">Section A + B</div>
      <div class="sc-meta">100 Questions &nbsp;&middot;&nbsp; 2 Hours</div>
      <div class="sc-meta" style="font-size:0.7rem;opacity:0.65;margin-top:3px;">Harder Quant, Reasoning + Advanced CS Topics</div>
    </div>
    <div class="set-card" id="card-3" onclick="selectSet('3')">
      <div class="sc-badge">Advanced</div>
      <div class="sc-num">Practice Set 3</div>
      <div class="sc-name">Section A + B + C</div>
      <div class="sc-meta">150 Questions &nbsp;&middot;&nbsp; 3 Hours</div>
      <div class="sc-meta" style="font-size:0.7rem;opacity:0.65;margin-top:3px;">Sec C: Digital Electronics, Microprocessors &amp; Embedded Systems</div>
    </div>
    <div class="set-card" id="card-4" onclick="selectSet('4')">
      <div class="sc-badge">Advanced</div>
      <div class="sc-num">Practice Set 4</div>
      <div class="sc-name">Section A + B</div>
      <div class="sc-meta">100 Questions &nbsp;&middot;&nbsp; 2 Hours</div>
      <div class="sc-meta" style="font-size:0.7rem;opacity:0.65;margin-top:3px;">Original Sample Paper &mdash; Advanced Level</div>
    </div>
  </div>
  <div id="set-info-panel" style="display:none">
    <div class="info-grid" id="set-info-grid"></div>
    <div style="font-size:0.85rem;opacity:0.7;margin-bottom:6px;">Exam begins at</div>
    <div id="start-time-label"></div>
    <div id="countdown-display">--:--:--</div>
    <div class="hint">Select a set above, then wait for the scheduled time or click Start</div>
    <button id="start-now-btn" onclick="startExam()" style="display:none;">Start Exam Now &#x25B6;</button>
  </div>
  <div style="margin-top:32px;opacity:0.45;font-size:0.75rem;letter-spacing:0.5px;">Prepared by &nbsp;<strong style="opacity:1;letter-spacing:1px;">Mohd Wamique (ex-CDACian)</strong></div>
</div>"""

# ================================================================
#  NEW JAVASCRIPT
# ================================================================
NEW_JS = r"""// ================================================================
//  CONFIG
// ================================================================
const CFG = {
  startTime: '2026-06-22T10:15:00+05:30',
  secDuration: 3600,
  marking: { correct: 3, wrong: -1 },
  submitEndpoint: 'https://formspree.io/f/xvzjgery'
};

// ================================================================
//  PRACTICE SETS
// ================================================================
const _K = [0x4D,0x77,0x51,0x7C,0x63,0x58,0x4F,0x52,0x71,0x39];

const SETS = {
  '1': { name:'Practice Set 1', level:'Normal', totalQ:100, sections:['A','B'], maxScore:300,
         ak:'__S1_AK__', questions:[
  __S1_Q__
  ]},
  '2': { name:'Practice Set 2', level:'Advanced', totalQ:100, sections:['A','B'], maxScore:300,
         ak:'__S2_AK__', questions:[
  __S2_Q__
  ]},
  '3': { name:'Practice Set 3', level:'Advanced + Section C', totalQ:150, sections:['A','B','C'], maxScore:450,
         ak:'__S3_AK__', questions:[
  __S3_Q__
  ]},
  '4': { name:'Practice Set 4', level:'Advanced', totalQ:100, sections:['A','B'], maxScore:300,
         ak:'__S4_AK__', questions:[__S4_Q__
  ]}
};

let CQ = [], CAK = [];

function initCurrentSet() {
  const set = SETS[S.selectedSet];
  CQ = set.questions;
  const b = atob(set.ak);
  CAK = Array.from(b).map((c,i) => (c.charCodeAt(0) ^ _K[i % _K.length]) - 65);
}

// ================================================================
//  STATE
// ================================================================
const SK = 'ccat_v5_' + (CFG.startTime || 'open');
let S = {
  selectedSet: null,
  sec: 'A', cur: 0,
  ans: new Array(150).fill(null),
  vis: new Array(150).fill(false),
  mrk: new Array(150).fill(false),
  tA: CFG.secDuration, tB: CFG.secDuration, tC: CFG.secDuration,
  aDone: false, bDone: false, done: false,
  nickname: '', startedAt: null
};
let ticker = null;

// ================================================================
//  HELPERS
// ================================================================
function getSectionRange(sec) {
  if (sec === 'A') return [0, 49];
  if (sec === 'B') return [50, 99];
  return [100, 149];
}

function renderQText(s) {
  return s.replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,'<br>');
}

function escH(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

// ================================================================
//  SET SELECTION
// ================================================================
function selectSet(id) {
  document.querySelectorAll('.set-card').forEach(c => c.classList.remove('selected'));
  const card = document.getElementById('card-' + id);
  if (card) card.classList.add('selected');
  S.selectedSet = id;
  initCurrentSet();
  saveS();
  showSetInfoPanel(id);
  const t0 = CFG.startTime ? new Date(CFG.startTime) : null;
  setStartLabel(t0);
  if (!t0 || Date.now() >= t0.getTime()) {
    document.getElementById('start-now-btn').style.display = 'inline-block';
    document.getElementById('countdown-display').textContent = 'READY';
  } else {
    document.getElementById('countdown-display').textContent = '--:--:--';
    countdownToStart(t0);
  }
}

function showSetInfoPanel(id) {
  const set = SETS[id];
  document.getElementById('set-info-grid').innerHTML =
    '<div class="info-tile"><div class="val">'+set.totalQ+'</div><div class="lbl">Questions</div></div>' +
    '<div class="info-tile"><div class="val">'+set.sections.length+' Hr'+(set.sections.length>1?'s':'')+'</div><div class="lbl">Duration</div></div>' +
    '<div class="info-tile"><div class="val">+3 / −1</div><div class="lbl">Marking</div></div>' +
    '<div class="info-tile"><div class="val">Sec '+set.sections.join('+')+'</div><div class="lbl">Sections</div></div>';
  document.getElementById('set-info-panel').style.display = 'block';
}

// ================================================================
//  BOOT
// ================================================================
window.addEventListener('load', () => {
  loadS();
  if (S.selectedSet) initCurrentSet();

  if (S.done && S.selectedSet)  { showResults(); return; }
  if (S.bDone && S.selectedSet && SETS[S.selectedSet].sections.includes('C')) { enterSection('C'); return; }
  if (S.aDone && S.selectedSet) { enterSection('B'); return; }

  if (S.selectedSet) {
    document.querySelectorAll('.set-card').forEach(c => c.classList.remove('selected'));
    const card = document.getElementById('card-' + S.selectedSet);
    if (card) card.classList.add('selected');
    showSetInfoPanel(S.selectedSet);
    const t0 = CFG.startTime ? new Date(CFG.startTime) : null;
    setStartLabel(t0);
    if (!t0 || Date.now() >= t0.getTime()) {
      document.getElementById('start-now-btn').style.display = 'inline-block';
      document.getElementById('countdown-display').textContent = 'READY';
    } else {
      countdownToStart(t0);
    }
  }
});

function setStartLabel(t0) {
  const el = document.getElementById('start-time-label');
  if (!el) return;
  el.textContent = t0
    ? t0.toLocaleString('en-IN',{weekday:'long',year:'numeric',month:'long',day:'numeric',hour:'2-digit',minute:'2-digit',timeZoneName:'short'})
    : 'Opens immediately when you load this page';
}

function countdownToStart(t0) {
  const el = document.getElementById('countdown-display');
  const tick = () => {
    const d = t0 - Date.now();
    if (d <= 0) { el.textContent = 'Starting…'; if (S.selectedSet) startExam(); return; }
    const h = String(Math.floor(d/3600000)).padStart(2,'0');
    const m = String(Math.floor(d%3600000/60000)).padStart(2,'0');
    const s = String(Math.floor(d%60000/1000)).padStart(2,'0');
    el.textContent = h+':'+m+':'+s;
  };
  tick(); setInterval(tick, 1000);
}

function startExam() {
  if (!S.selectedSet) { alert('Please select a practice set first.'); return; }
  document.getElementById('waiting-screen').style.display = 'none';
  const sub = document.getElementById('name-screen-sub');
  if (sub) {
    const set = SETS[S.selectedSet];
    sub.textContent = set.name+' ('+set.level+') | '+set.totalQ+' Questions | '+set.sections.length+' Hour'+(set.sections.length>1?'s':'');
  }
  document.getElementById('name-screen').style.display = 'flex';
}

function checkProceed() {
  const name = document.getElementById('nickname-input').value.trim();
  const checked = document.getElementById('consent-chk').checked;
  document.getElementById('proceed-btn').classList.toggle('ready', name.length > 0 && checked);
}

function proceedToExam() {
  const name = document.getElementById('nickname-input').value.trim();
  if (!name) return;
  S.nickname = name; S.startedAt = Date.now(); saveS();
  document.getElementById('name-screen').style.display = 'none';
  enterSection('A');
}

function enterSection(sec) {
  S.sec = sec;
  const [start] = getSectionRange(sec);
  S.cur = start; S.vis[start] = true;
  document.getElementById('waiting-screen').style.display = 'none';
  document.getElementById('name-screen').style.display   = 'none';
  document.getElementById('exam-screen').style.display   = 'flex';
  const nn = document.getElementById('header-nickname');
  if (nn) nn.textContent = S.nickname ? 'Candidate: '+S.nickname : '';
  buildPalette(); renderQ(); runTimer(); saveS();
}

// ================================================================
//  TIMER
// ================================================================
function runTimer() {
  if (ticker) clearInterval(ticker);
  updateTimerUI();
  ticker = setInterval(() => {
    let timeUp = false;
    if      (S.sec==='A') { S.tA--; if (S.tA<=0) { S.tA=0; timeUp=true; } }
    else if (S.sec==='B') { S.tB--; if (S.tB<=0) { S.tB=0; timeUp=true; } }
    else                  { S.tC--; if (S.tC<=0) { S.tC=0; timeUp=true; } }
    if (timeUp) {
      clearInterval(ticker); saveS();
      if (S.sec==='A') endSection('A',true);
      else if (S.sec==='B' && SETS[S.selectedSet].sections.includes('C')) endSection('B',true);
      else submit();
      return;
    }
    const left = S.sec==='A' ? S.tA : S.sec==='B' ? S.tB : S.tC;
    if (left<=300) document.getElementById('timer-display').classList.add('warning');
    updateTimerUI(); saveS();
  }, 1000);
}

function updateTimerUI() {
  const secs = S.sec==='A' ? S.tA : S.sec==='B' ? S.tB : S.tC;
  const m = String(Math.floor(secs/60)).padStart(2,'0');
  const s = String(secs%60).padStart(2,'0');
  document.getElementById('timer-display').textContent = m+':'+s;
  const labels = {
    'A':'Section A — English, Quantitative Aptitude & Reasoning (Q1–50)',
    'B':'Section B — Computer Fundamentals, C, DS, OOP, OS & Networking (Q51–100)',
    'C':'Section C — Digital Electronics, Microprocessors & Embedded Systems (Q101–150)'
  };
  document.getElementById('section-label').textContent = labels[S.sec]||'';
  const [start] = getSectionRange(S.sec);
  const answered = S.ans.slice(start,start+50).filter(x=>x!==null).length;
  document.getElementById('progress-text').textContent = 'Answered: '+answered+' / 50';
}

// ================================================================
//  SECTION TRANSITION
// ================================================================
function endSection(sec, auto) {
  if (sec==='A') S.aDone=true; else S.bDone=true;
  saveS();
  const nextSec   = sec==='A' ? 'B' : 'C';
  const nextLabel = nextSec==='B' ? 'Section B' : 'Section C';
  document.getElementById('modal-title').textContent = auto ? 'Section '+sec+' Time Up!' : 'Section '+sec+' Submitted';
  document.getElementById('modal-body').textContent  = auto
    ? 'Time for Section '+sec+' has expired. Your answers are saved. Click below to start '+nextLabel+'. A fresh 60-minute timer will begin.'
    : 'You have submitted Section '+sec+' early. You cannot return. Click below to start '+nextLabel+'.';
  document.getElementById('sec-modal-btn').textContent = 'Start '+nextLabel+' →';
  document.getElementById('sec-modal').classList.add('show');
}

function beginNextSection() {
  document.getElementById('sec-modal').classList.remove('show');
  document.getElementById('timer-display').classList.remove('warning');
  enterSection(S.sec==='A' ? 'B' : 'C');
}

function confirmSubmit() {
  const set = SETS[S.selectedSet];
  if (S.sec==='A') {
    if (confirm('Submit Section A and move to Section B? You cannot return.')) { clearInterval(ticker); endSection('A',false); }
  } else if (S.sec==='B' && set.sections.includes('C')) {
    if (confirm('Submit Section B and move to Section C? You cannot return.')) { clearInterval(ticker); endSection('B',false); }
  } else {
    if (confirm('Submit the exam? This is final.')) { clearInterval(ticker); submit(); }
  }
}

function submit() { S.done=true; saveS(); sendSnapshot(); showResults(); }

// ================================================================
//  PALETTE
// ================================================================
function buildPalette() {
  const [start] = getSectionRange(S.sec);
  const g = document.getElementById('palette-grid');
  g.innerHTML = '';
  for (let i=start; i<start+50; i++) {
    const b = document.createElement('button');
    b.className = 'palette-btn'; b.textContent = i+1; b.dataset.i = i;
    b.addEventListener('click', () => goTo(i));
    g.appendChild(b);
  }
  refreshPalette();
}

function refreshPalette() {
  const [start] = getSectionRange(S.sec);
  let sa=0, sn=0, sm=0, sv=0;
  for (let i=start; i<start+50; i++) {
    const b = document.querySelector('.palette-btn[data-i="'+i+'"]');
    if (!b) continue;
    b.className = 'palette-btn';
    const answered=S.ans[i]!==null, marked=S.mrk[i], visited=S.vis[i];
    if (answered && marked) { b.classList.add('ans-marked'); sm++; }
    else if (answered)       { b.classList.add('answered');  sa++; }
    else if (marked)         { b.classList.add('marked');    sm++; }
    else if (visited)        { b.classList.add('visited');   sn++; }
    else                     { sv++; }
    if (i===S.cur) b.classList.add('current');
  }
  document.getElementById('s-ans').textContent=sa;
  document.getElementById('s-not').textContent=sn;
  document.getElementById('s-mrk').textContent=sm;
  document.getElementById('s-nv').textContent=sv;
}

// ================================================================
//  QUESTION RENDERING
// ================================================================
function renderQ() {
  const q = CQ[S.cur];
  if (!q) return;
  document.getElementById('q-number').textContent  = 'Question '+q.id+' of '+CQ.length;
  document.getElementById('q-cat-tag').textContent = q.cat;
  document.getElementById('q-text').innerHTML      = renderQText(q.q);
  const list = document.getElementById('opts-list');
  list.innerHTML = '';
  ['A','B','C','D'].forEach((lbl, i) => {
    const div = document.createElement('div');
    div.className = 'opt-item'+(S.ans[S.cur]===i?' selected':'');
    div.innerHTML = '<div class="opt-letter">'+lbl+'</div><span></span>';
    div.querySelector('span').innerHTML = renderQText(q.o[i]);
    div.addEventListener('click', () => pick(i));
    list.appendChild(div);
  });
  const rb = document.getElementById('btn-review');
  rb.textContent = S.mrk[S.cur] ? '★ Marked' : 'Mark for Review';
  rb.classList.toggle('on', S.mrk[S.cur]);
  const [start] = getSectionRange(S.sec);
  document.getElementById('btn-prev').disabled = (S.cur===start);
  refreshPalette();
  document.querySelector('.palette-btn[data-i="'+S.cur+'"]')?.scrollIntoView({block:'nearest'});
}

function pick(i) {
  S.ans[S.cur]=i;
  document.querySelectorAll('.opt-item').forEach((el,idx)=>el.classList.toggle('selected',idx===i));
  refreshPalette(); saveS();
}

function navigate(dir) {
  const [start,end] = getSectionRange(S.sec);
  const n = S.cur+dir;
  if (n<start||n>end) return;
  S.cur=n; S.vis[n]=true; renderQ(); saveS();
}

function goTo(i) { S.cur=i; S.vis[i]=true; renderQ(); saveS(); }

function toggleReview() {
  S.mrk[S.cur]=!S.mrk[S.cur];
  const rb=document.getElementById('btn-review');
  rb.textContent=S.mrk[S.cur]?'★ Marked':'Mark for Review';
  rb.classList.toggle('on',S.mrk[S.cur]);
  refreshPalette(); saveS();
}

// ================================================================
//  PERSISTENCE
// ================================================================
function saveS() { try { localStorage.setItem(SK,JSON.stringify(S)); } catch(e){} }
function loadS() {
  try { const d=localStorage.getItem(SK); if(d) Object.assign(S,JSON.parse(d)); } catch(e){}
}

// ================================================================
//  RESULTS
// ================================================================
function calcStats() {
  const set = SETS[S.selectedSet];
  let cor=0, wrg=0, una=0;
  CQ.forEach((q,i) => {
    if (S.ans[i]===null) una++;
    else if (S.ans[i]===CAK[i]) cor++;
    else wrg++;
  });
  const score    = cor*CFG.marking.correct + wrg*CFG.marking.wrong;
  const negMarks = wrg*Math.abs(CFG.marking.wrong);
  const spentA   = CFG.secDuration-S.tA;
  const spentB   = CFG.secDuration-S.tB;
  const spentC   = set.sections.includes('C') ? CFG.secDuration-S.tC : 0;
  const totalSec = spentA+spentB+spentC;
  const fmt = s => String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');
  return { cor, wrg, una, score, negMarks, spentA, spentB, spentC, totalSec, fmt };
}

function showResults() {
  ['waiting-screen','name-screen','exam-screen'].forEach(id => document.getElementById(id).style.display='none');
  document.getElementById('results-screen').style.display='block';
  const set = SETS[S.selectedSet];
  const { cor, wrg, una, score, negMarks, spentA, spentB, spentC, totalSec, fmt } = calcStats();
  document.getElementById('res-header').querySelector('p').innerHTML =
    (S.nickname?'Candidate: <strong>'+escH(S.nickname)+'</strong> &nbsp;|&nbsp; ':'')+
    escH(set.name)+' ('+escH(set.level)+') &nbsp;|&nbsp; Marking: +3 correct, −1 wrong';
  const allBtn = document.getElementById('filter-all-btn');
  if (allBtn) allBtn.textContent = 'All '+set.totalQ;
  let secT =
    '<div class="score-tile" style="border-left:3px solid #1565c0;"><div class="s-val" style="color:#1565c0;">'+fmt(spentA)+'</div><div class="s-lbl">Section A Time</div></div>'+
    '<div class="score-tile" style="border-left:3px solid #1565c0;"><div class="s-val" style="color:#1565c0;">'+fmt(spentB)+'</div><div class="s-lbl">Section B Time</div></div>';
  if (set.sections.includes('C'))
    secT += '<div class="score-tile" style="border-left:3px solid #1565c0;"><div class="s-val" style="color:#1565c0;">'+fmt(spentC)+'</div><div class="s-lbl">Section C Time</div></div>';
  document.getElementById('score-grid').innerHTML =
    '<div class="score-tile t"><div class="s-val">'+score+'</div><div class="s-lbl">Total Score (max '+set.maxScore+')</div></div>'+
    '<div class="score-tile c"><div class="s-val">'+cor+'</div><div class="s-lbl">Correct (+'+CFG.marking.correct+' each)</div></div>'+
    '<div class="score-tile w"><div class="s-val">'+wrg+'</div><div class="s-lbl">Wrong ('+CFG.marking.wrong+' each)</div></div>'+
    '<div class="score-tile u"><div class="s-val">'+una+'</div><div class="s-lbl">Unattempted</div></div>'+
    '<div class="score-tile" style="border-left:3px solid #b71c1c;"><div class="s-val" style="color:#b71c1c;">−'+negMarks+'</div><div class="s-lbl">Negative Marks</div></div>'+
    secT+
    '<div class="score-tile" style="border-left:3px solid #37474f;"><div class="s-val" style="color:#37474f;">'+fmt(totalSec)+'</div><div class="s-lbl">Total Time Taken</div></div>';
  renderSolutions('all');
}

async function sendSnapshot() {
  if (!CFG.submitEndpoint) return;
  const set = SETS[S.selectedSet];
  const { cor, wrg, una, score, negMarks, spentA, spentB, spentC, totalSec, fmt } = calcStats();
  const body = {
    nickname: S.nickname||'(no name)',
    practice_set: set.name+' ('+set.level+')',
    score, correct:cor, wrong:wrg, unattempted:una,
    negative_marks: '-'+negMarks,
    section_a_time: fmt(spentA),
    section_b_time: fmt(spentB),
    total_time: fmt(totalSec),
    submitted_at: new Date().toLocaleString('en-IN',{timeZone:'Asia/Kolkata'})
  };
  if (set.sections.includes('C')) body.section_c_time = fmt(spentC);
  try {
    await fetch(CFG.submitEndpoint,{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify(body)
    });
  } catch(e){}
}

function renderSolutions(filter) {
  const L = ['A','B','C','D'];
  const container = document.getElementById('sol-list');
  container.innerHTML = '';
  CQ.forEach((q,i) => {
    const ua=S.ans[i], isC=ua===CAK[i], isU=ua===null, isW=!isC&&!isU;
    if (filter==='c'&&!isC) return;
    if (filter==='w'&&!isW) return;
    if (filter==='u'&&!isU) return;
    const status = isC?'✓ Correct':isW?'✗ Wrong (you chose '+L[ua]+')':'— Unattempted';
    const optsH = q.o.map((opt,oi) => {
      let cls='sol-opt';
      if (oi===CAK[i]) cls+=' ca';
      if (oi===ua&&!isC) cls+=' wa';
      return '<span class="'+cls+'">'+L[oi]+': '+renderQText(opt)+'</span>';
    }).join('');
    const secBadge = q.s==='C'?' | Sec C':q.s==='B'?' | Sec B':' | Sec A';
    const d = document.createElement('div');
    d.className = 'sol-item '+(isC?'c':isW?'w':'u');
    d.innerHTML =
      '<div class="sol-meta">Q'+q.id+secBadge+' &nbsp;|&nbsp; '+escH(q.cat)+' &nbsp;|&nbsp; <strong>'+status+'</strong></div>'+
      '<div class="sol-q">'+renderQText(q.q)+'</div>'+
      '<div class="sol-opts">'+optsH+'</div>'+
      (q.exp?'<div class="sol-exp"><strong>Explanation:</strong> '+renderQText(q.exp)+'</div>':'');
    container.appendChild(d);
  });
}

function restartExam() {
  if (confirm('This will clear your exam and return to the start. Are you sure?')) {
    localStorage.removeItem(SK); window.location.reload();
  }
}

function savePDF() {
  document.querySelectorAll('.f-btn').forEach(b=>b.classList.remove('on'));
  document.querySelector('.f-btn').classList.add('on');
  renderSolutions('all');
  setTimeout(()=>window.print(),150);
}

function filterSol(type,btn) {
  document.querySelectorAll('.f-btn').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on'); renderSolutions(type);
}

// ================================================================
//  SECURITY
// ================================================================
(function(){
  document.addEventListener('contextmenu', e => {
    if (document.getElementById('exam-screen').style.display!=='none') e.preventDefault();
  });
  document.addEventListener('keydown', e => {
    const exam=document.getElementById('exam-screen').style.display!=='none';
    if (!exam) return;
    const bad=(e.key==='F12')||(e.ctrlKey&&e.shiftKey&&['I','J','C'].includes(e.key.toUpperCase()))||(e.ctrlKey&&e.key.toUpperCase()==='U');
    if (bad){e.preventDefault();e.stopPropagation();}
  },true);
  const THRESH=160; let dtOpen=false;
  const overlay=document.createElement('div');
  overlay.id='dt-overlay';
  overlay.innerHTML='<div style="background:white;padding:40px 32px;border-radius:12px;text-align:center;max-width:380px;box-shadow:0 8px 32px rgba(0,0,0,0.3)"><div style="font-size:2rem;margin-bottom:12px;">⚠️</div><h2 style="color:#b71c1c;margin-bottom:10px;">Developer Tools Detected</h2><p style="color:#444;line-height:1.6">Close Developer Tools to continue the exam.<br>The timer is still running.</p></div>';
  Object.assign(overlay.style,{display:'none',position:'fixed',inset:'0',background:'rgba(0,0,0,0.85)',zIndex:'9999',alignItems:'center',justifyContent:'center'});
  document.body.appendChild(overlay);
  setInterval(()=>{
    const exam=document.getElementById('exam-screen').style.display!=='none';
    if (!exam) return;
    const open=(window.outerWidth-window.innerWidth>THRESH)||(window.outerHeight-window.innerHeight>THRESH);
    if (open!==dtOpen){dtOpen=open;overlay.style.display=open?'flex':'none';}
  },800);
})();"""

# ================================================================
#  APPLY CHANGES TO HTML
# ================================================================

# 1. Add CSS
html = html.replace('</style>', NEW_CSS + '\n</style>', 1)

# 2. Update title
html = html.replace(
    '<title>CDAC C-CAT Mock Test – Practice Set 4</title>',
    '<title>CDAC C-CAT Mock Test – Practice Sets 1–4</title>'
)

# 3. Replace waiting screen (use comment markers as boundaries to handle nested divs)
ws_start = '<!-- ============ WAITING SCREEN ============ -->'
ws_end   = '<!-- ============ NAME SCREEN'
ws_start_idx = html.index(ws_start)
ws_end_idx   = html.index(ws_end, ws_start_idx)
html = html[:ws_start_idx] + ws_start + '\n' + NEW_WAITING + '\n\n' + html[ws_end_idx:]

# 4. Update name screen subtitle to be dynamic
html = html.replace(
    '<div class="sub">CDAC C-CAT Practice Set 4 (Advanced) &nbsp;|&nbsp; 100 Questions &nbsp;|&nbsp; 2 Hours</div>',
    '<div class="sub" id="name-screen-sub">CDAC C-CAT Practice Test</div>'
)

# 5. Update section modal button id
html = html.replace(
    '<button onclick="beginSectionB()">Start Section B →</button>',
    '<button id="sec-modal-btn" onclick="beginNextSection()">Start Section B →</button>'
)
# Also handle ASCII arrow version
html = html.replace(
    '<button onclick="beginSectionB()">Start Section B &rarr;</button>',
    '<button id="sec-modal-btn" onclick="beginNextSection()">Start Section B &rarr;</button>'
)

# 6. Add id to filter-all button
html = html.replace(
    "onclick=\"filterSol('all',this)\">All 100</button>",
    "id=\"filter-all-btn\" onclick=\"filterSol('all',this)\">All 100</button>"
)

# 7. Replace script section
script_pat = re.compile(r'<script>.*?</script>', re.DOTALL)

# Perform substitutions in NEW_JS
final_js = NEW_JS
final_js = final_js.replace('__S1_AK__', s1_ak)
final_js = final_js.replace('__S2_AK__', s2_ak)
final_js = final_js.replace('__S3_AK__', s3_ak)
final_js = final_js.replace('__S4_AK__', s4_ak)
final_js = final_js.replace('  __S1_Q__\n', '  ' + s1_qs.replace('\n', '\n  ') + '\n')
final_js = final_js.replace('  __S2_Q__\n', '  ' + s2_qs.replace('\n', '\n  ') + '\n')
final_js = final_js.replace('  __S3_Q__\n', '  ' + s3_qs.replace('\n', '\n  ') + '\n')
final_js = final_js.replace('__S4_Q__', q4_content)

script_replacement = '<script>\n' + final_js + '\n</script>'
html = script_pat.sub(lambda m: script_replacement, html)

# ================================================================
#  WRITE OUTPUT
# ================================================================
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = len(html) / 1024
print(f"Done! Written to {HTML_PATH}")
print(f"File size: {size_kb:.1f} KB")
