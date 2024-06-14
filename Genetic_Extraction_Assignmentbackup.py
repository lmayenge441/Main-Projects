# Demonstrating assigning variables
# STUDENT NAME: LYDIA MAYENGE
# This code allows me to print on the screen


DNA_nucleotide_1 ="A"
DNA_nucleotide_2 ="T"
DNA_nucleotide_3 ="C"
DNA_nucleotide_4 ="G"
DNA_nucleotide_list = ["A", "T", "C", "G"]


start_codon = "ATG"          # start condon is ATG
start_codon_list = []         # list for start condon

stop_codon_1 = "ATC"          # stop condon 1 is TAG
stop_codon_2 = "TAA"          # stop condon 2 is TAA
stop_codon_3 = "TAG"          # stop condon 3 is TGA
stop_codon_list = ["ATC", "TAA", "TAG"] # list for stop condon

#______________________________________________________________
choice_input= str(input("Enter a DNA sequence(or enter stop): "))

while choice_input != 'stop':
    start_codon_list = []
    counter =0
    counter1= 3
    start_codon_counter=0
    Number_of_codons= 0 
    #DNA_sequence="CTCGATGCTATGGATGCTATGCTCGATGCTATGGATGCTTAA"
    DNA_sequence= choice_input
    DNA_sequence_length = len(DNA_sequence) # DNA sequence length
    print (DNA_sequence)
    print("The length of the DNA sequence",DNA_sequence ,"is", len(DNA_sequence))
    Number_of_codons=len(DNA_sequence)/3
    print("There are ",Number_of_codons , "DNA codon(s)")
# DNA sequnce string is set to empty
    DNA_sequence_string=" "
#------------------------------------------------------------------
#start of while loop
    while (counter < DNA_sequence_length):  
        DNA_codon =DNA_sequence[counter:counter1] 
        if DNA_codon == start_codon:
            start_codon_counter=start_codon_counter+1
        # Append start codon list
            start_codon_list.append(counter)
        
        # add the start codon onto the string
            DNA_sequence_string= DNA_sequence_string + DNA_codon
        else:
           DNA_sequence_string= DNA_sequence_string + DNA_codon
        counter = counter +3
        counter1= counter1+3
    
# end of while loop
#----------------------------------------------------------------
# verify the last condom is a stop codom
#-------------------------------------------------
    if DNA_codon != (stop_codon_3 or stop_codon_1 or stop_codon_2):
        DNA_sequence_string=" - "
#-------------------------------------------------
    #print("The start codon list is",start_codon_list)
    print("There are",len(start_codon_list)," start condons in the sequence")
#------------------------------------------------------------------
# Printing all sequences with start condons
    counter =0
    while (counter < len(start_codon_list)):  
         DNA_sequence_string_output = DNA_sequence_string[start_codon_list[counter]+1:len(DNA_sequence)+1]
         counter = counter+1
         print("DNA sequence number",counter," is",DNA_sequence_string_output)
    
# end of while loop-----------------------------------------------
    choice_input= str(input("Enter a DNA sequence(or stop to end): "))
