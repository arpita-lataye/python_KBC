print('🙏welcome to KBC🙏')
quetion_list=['how many continents are there🤔?',
             'what is the capital of india🤔?',
             'which courses are taught in navgurukul🤔?']
options_list=[['four','nine','seven','eight'],
         ['chandigarh','bhopal','chennai','delhi'],
         ['software engineering','counseling','tourism','agriculture']]
solution=[3,4,1]
lifiline_options=[['four','seven'],
                ['bhopal','delhi'],
                ['software engineering','tourism']]  
i=0
count=0
while i<len(quetion_list):
    print(i+1,quetion_list[i])
    j=0
    while j<len(options_list[i]):
        print(" ",j+1,options_list[i][j])
        j=j+1
    lifeline=input('do you want to use 50-50 lifeline😯:1yes, 2.no:')
    if lifeline=='1':  
        count=count+1
        if count==1:
            j=0
            while j<len(lifiline_options[i]):
                print(j+1,lifiline_options[i][j])  
                j=j+1
            ans1=int(input('select one option:'))
            sol=[2,2,1]
            rp=[10000,100000,10000000]
            if ans1==sol[i]:
                print("yahoooo🥳!,your answer is correct and you get rs",rp[i]," check😁")
                print('your next quetion is')
            else:
                print("ooho😟 your answer is wrong,you are out of the game now.") 
                break 
        else:
            print('Sorry😔!,you have already😌 use lifeline')  
            k=0
            while k<len(options_list[i]):
                print(' ',k+1,options_list[i][k])
                k=k+1
            ans=int(input('select your answer:'))
            rs=[10000,100000,10000000]
            if ans==solution[i]:
                print('congrats🥳!,your ans is correct')
                print('you get rs',rs[i],'check😁')
                # print('your next quetion is')
            else:
                print("sorry your answer is wrong,you are out😧 of the game now.") 
                break
    else:    
        ans=int(input('select your answer:'))
        rs=[10000,100000,10000000]
        if ans==solution[i]:
            print('congrats🥳!,your answer is correct')
            print('you get rs',rs[i],'check😁')
            # print('your next quetion is')
        else:
            print('oops😔,your answer is wrong,you are out😧 of the game now.')
            break
    i=i+1
print('🥳CONGRATULATIONS🥳 you have won😄 the game.')
print('you get total',11100000,'caror check😯😁')