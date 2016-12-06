def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    temp=tagger.tag(word.split())[0][1]
    gazLoc="0"
    gazPer="0"
    gazOrg="0"
    if(temp=='ORGANIZATION'):
        gazOrg="1"
    if(temp=='LOCATION'):
        gazLoc="1"
    if(temp=='PERSON'):
        gazPer="1"
    
    location_suffix_trigger=set(['city','street','river','boulevard'])
    location_prefix_trigger=set(['at'])
    person_prefix_trigger=set(['mr.','mrs.','dr.'])
    organization_suffix_trigger=set(['ltd','ltd.','co','co.','corp','corp.','corporation'])
    isPersonTrigger="0"
    isprefixLocationTriger="0"
    issuffixLocationTrigger="0"
    isOrganisationTrigger="0"
    
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        'postag=' + postag,
        'postag[:2]=' + postag[:2],
        'gazOrg=' + gazOrg,
        'gazLoc=' + gazLoc,
        'gazPer=' + gazPer,
    ]
    
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        if(word1 in location_prefix_trigger):
            isprefixLocationTriger="1"
        if(word1 in person_prefix_trigger):
            isPersonTrigger="1"
     
            
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:postag=' + postag1,
            '-1:postag[:2]=' + postag1[:2],
             'isprefixLocationTriger=' + isprefixLocationTriger,
             'isPersonTrigger=' + isPersonTrigger,  
        ])
    else:
        features.append('BOS')
        
    if i < len(sent)-1:
                
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        if(word1 in location_suffix_trigger):
            issuffixLocationTrigger="1"
        if(word1 in organization_suffix_trigger):
            isOrganisationTrigger="1" 
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:postag=' + postag1,
            '+1:postag[:2]=' + postag1[:2],
            'issuffixLocationTrigger=' + issuffixLocationTrigger,
            'isOrganisationTrigger=' + isOrganisationTrigger,
        ])
    else:
        features.append('EOS')
                
    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [token for token, postag, label in sent]



