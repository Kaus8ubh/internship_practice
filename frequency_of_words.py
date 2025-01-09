para = """ A paragraph is a series of sentences that are organized and coherent, and are all related 
           to a single topic. Almost every piece of writing you do that is longer than a few sentences 
           should be organized into paragraphs. This is because paragraphs show a reader where the subdivisions 
           of an essay begin and end, and thus help the reader see the organization of the essay and grasp its main points """
      
def occurance_of_words(para):
  dict={}
  drops=["A","a","the","The","is","Is","of","Of","and",
         "And","to","To","in","In","for","For","on","are",
         "On","with","With","that","That","by","By","this","They","These"," "]
  words=para.split()
  for word in words:
    if word in drops:
      continue
    if word in dict:
      dict[word]+=1
    else:
      dict[word]=1
  return dict

print(occurance_of_words(para))
