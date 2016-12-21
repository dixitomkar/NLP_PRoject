''' 
This program is for extracting the features. Use output of this file to Weka. 
'''
import nltk
sent=[]
a=pd.read_csv('trainfile', sep=" ", header = None) 
all_words=a.as_matrix()
location_suffix_trigger=set(['city','street','river','boulevard'])
location_prefix_trigger=set(['at'])
person_prefix_trigger=set(['mr.','mrs.','dr.'])
organization_suffix_trigger=set(['ltd','ltd.','co','co.','corp','corp.','corporation'])
st_line=0
file2 = open('with_tags_train.txt', 'w')

#print("Word>Length>POS-Tag>isFirstLetterUpper>isAllupper>isPersonTrigger>isprefixLocationTriger>issuffixLocationTrigger>isOrganisationTrigger>TrainLabel>TrainLabel_IOB")
file2.write("Word>Length>POS-Tag>isFirstLetterUpper>isAllupper>isPersonTrigger>isprefixLocationTriger>issuffixLocationTrigger>isOrganisationTrigger>TrainLabel>TrainLabel_IOB")
file2.write('\n')
for i in range(0,len(all_words)):
#for i in range(0,49):
    if(all_words[i][0]=='end_of_sentence'):
        tags=nltk.pos_tag(sent)
        for j in range(0,len(tags)):
            isPersonTrigger="0"
            isprefixLocationTriger="0"
            issuffixLocationTrigger="0"
            isOrganisationTrigger="0"
            word=tags[j][0].lower()
            word_prev=tags[j-1][0].lower()
            if(j!=len(tags)-1):
                word_next=tags[j+1][0].lower()
            else:
                word_next='thullu'
            if(word_prev in location_prefix_trigger):
                isprefixLocationTriger="1"
            if(word_prev in person_prefix_trigger):
                isPersonTrigger="1"
            if(word_next in location_suffix_trigger):
                issuffixLocationTrigger="1"
            if(word_next in organization_suffix_trigger):
                isOrganisationTrigger="1"             
            
            #print(tags[j][0],">",len(tags[j][0]),">",tags[j][1], ">",tags[j][0].istitle(), ">", tags[j][0].isupper(),isPersonTrigger,">",isprefixLocationTriger,">",issuffixLocationTrigger,">",isOrganisationTrigger,">",all_words[st_line][1],">",all_words[st_line][2])
            op_str=tags[j][0]+">"+str(len(tags[j][0]))+">"+tags[j][1]+ ">"+str(tags[j][0].istitle())+ ">"+ str(tags[j][0].isupper())+">"+isPersonTrigger+">"+isprefixLocationTriger+">"+issuffixLocationTrigger+">"+isOrganisationTrigger+">"+all_words[st_line][1]+">"+all_words[st_line][2]

            file2.write(op_str)
            file2.write('\n')

            st_line=st_line+1
        sent=[]
        st_line=i+1
    else:
        sent.append(all_words[i][0])

file2.close()
print("COmplete")        
            
