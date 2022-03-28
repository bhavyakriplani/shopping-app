print("  *** WELCOME TO THE SHOPPY SHOP ***")
adminid="GLA"
adminpassward="1000"
sum=0
u1="ram"
p1="123"
u2="shyam"
p2="345"
u3="sohit"
p3="567"
counter=0
count=0
want =1
hp=20
dell=20
apple=20
boath=20
samh=20
realmeh=20
iphn=20
sams=20
onepls=20
canon=20 
sony=20
nikon=20
strner=20
trimr=20
cler=20
sirts=20
sirtm=20
sirtl=20
tsirts=20
tsirtm=20
tsirtl=20
jens=20
jenm=20
jenl=20
cass=20
casm=20
casl=20
forms=20
formm=20
forml=20
slips=20
slipm=20
slipl=20
kurws=20
kurwm=20
kurwl=20
sare=20
tops=20
topm=20
topl=20
shoes=20
shoem=20
shoel=20
heels=20
heelm=20
heell=20
sandls=20
sandlm=20
sandll=20
dres=20
drem=20
drel=20
js=20
jm=20
jl=20
ews=20
ewm=20
ewl=20
shks=20
shkm=20
shkl=20
sandks=20
sandkm=20
sandkl=20
slipks=20
slipkm=20
slipkl=20
serum=20
facwas=20
lotn=20
sampo=20
cnditnr=20
hrol=20
deo=20
prfm=20
rol=20
while(1):
    print('''
             1.Press A if you are Admin
             2.Press U if you are User
             3.Press N if you want to close the App
             4.Press B if you want to browse without logging in
             5.Press E if you want to exit''')
    a=input("Enter your Identity-->  ")
    a=a.upper()
    if a=='A':
        print("  Welcome to the Admin Panel")
        aid=input("    Enter your Login ID  ")
        if aid==adminid:
            apss=input("Enter the Login Passward--  ")
            if apss==adminpassward:
                print("Login to Admin Panel Done Successfully")
                b=int(input("Enter 1 for Stock View and 2 for Stock Management-->"))
                if b==1:
                    print("Welcome to the Stock View Panel")
                    print(f'''
                          ELECTRONNICS ITEMS:-
                         __________________________
                          #:-Laptops:-
                           1. HP    (Thin and Light Laptop)       ={hp}
                           2. Dell  (Ultra Light Weight)          ={dell} 
                           3. Apple (Ultra Light and Long Lasting)={apple}
                           
                          #:-Headphones:-
                           4. Boat    (Bluetooth Headset)           ={boath}
                           5. Samsung (Truly Wireless Headphones)   ={samh}
                           6. Realme  (Silicon Neckband and Earwing)={realmeh}
                           
                          #.Cameras:-
                           7. Canon (Sports and Action Camera)={canon}
                           8. Sony  (Perfect for Beginners)   ={sony}
                           9. Nikon (Digital Zoom Camera)     ={nikon}
                           
                          #:-Mobile Phones:-
                           10. Iphone  (ios 14)           ={iphn}
                           11. Samsung (Android 11)       ={sams}
                           12. Oneplus (5g Phone)         ={onepls}
                          
                          #:- Styling Gadgets:-
                           13. Straightner (Nova Smooth)={strner}
                           14. Trimmer (Chargable)      ={trimr}
                           15. Curler (Electric Curler) ={cler}
                           
                           FASHION
                          _____________ 
                           #:-For Men :-
                           # Clothing
                           16. Shirt (Small Size)   ={sirts}
                           17.Shirt (Medium Size)  ={sirtm}
                           18.Shirt (Large Size)   ={sirtl}
                           19.T-Shirt (Small Size) ={tsirts}
                           20.T-Shirt (Medium Size)={tsirtm}
                           21.T-Shirt (Large Size) ={tsirtl}
                           22.Jeans (Small Size)   ={jens}
                           23.Jeans (Medium Size)  ={jenm}
                           24.Jeans  ( Large Size) ={jenl}
                           
                           # Footwear
                           25.Casual (Small Size)   ={cass}
                           26.Casual (Medium Size)  ={casm}
                           27.Casual (Large Size)   ={casl}
                           28.Formal (Small Size)   ={forms}
                           29.Formal (Medium Size)  ={formm}
                           30.Formal (Large Size)   ={forml}
                           31.Slippers (Small Size) ={slips}
                           32.Slippers (Medium Size)={slipm}
                           33.Slippers (Large Size) ={slipl}
                           
                           #:-For Women :-
                           # Clothing
                           34.Kurta (Small Size)         ={kurws}
                           35.Kurta (Medium Size)        ={kurwm}
                           36.Kurta (Large Size)         ={kurwl}
                           37.Saree (Shiny and Silk Made)={sare}
                           38.Girls Tops (Small Size)    ={tops}
                           39.Girls Tops (Medium Size)   ={topm}
                           40.Girls Tops (Large Size)    ={topl}
                           
                           #Footwear
                           41.Shoes (Small Size Women Shoes)   ={shoes}
                           42.Shoes (Medium Size Women Shoes)  ={shoem}
                           43.Shoes (Large Size Women Shoes)   ={shoel}
                           44.Heels (Small Size Women Heels)   ={heels}
                           45.Heels (Medium Size Women Heels)  ={heelm}
                           46.Heels (Large Size Women Heels)   ={heell}
                           47.Sandle (Small Size Women Sandle) ={sandls}
                           48.Sandle (Medium Size Women Sandle)={sandlm}
                           49.Sandle (Large Size Women Sandle) ={sandll}
                           
                           #:-For Kids :-
                           #Clothing
                           50.Dress (Small Size Dress For kids)  ={dres}
                           51.Dress (Medium Size Dress for kids) ={drem}
                           52.Dress (Large Size Dress for kids)  ={drel}
                           53.Jeans (Small Size Jeans for Kids)  ={js}
                           54.Jeans (Medium Size Jeans for Kids) ={jm}
                           55.Jeans (Large Size Jeans for Kids)  ={jl}
                           56.Ethnic Wears (Small Size for Kids) ={ews}
                           57.Ethnic Wears (Medium Size for Kids)={ewm}
                           58.Ethnic Wears (Large Size for Kids) ={ewl}
                           
                           #Footwear
                           59.Shoes (Small Size Shoes For Kids)       ={shks}
                           60.Shoes (Medium Size Shoes For Kids)      ={shkm}
                           61.Shoes (Large Size Shoes For Kids)       ={shkl}
                           62.Sandals (Small Size Sandals For Kids)   ={sandks}
                           63.Sandals (Medium Size Sandals For Kids)  ={sandkm}
                           64.Sandals (Large Size Sandals For Kids)   ={sandkl}
                           65.Slippers (Small Size Slippers for Kids) ={slipks}
                           66.Slippers (Medium Size Slippers for Kids)={slipkm}                                                 
                           67.Slippers (Large Size Slippers for Kids) ={slipkl}
                           
                           Beauty Destination
                         _________________________
                         #:- Skin Care :-
                         68.Serum   ={serum}
                         69.Facewash={facwas}
                         70.Lotion  ={lotn}
                         
                         #:-Hair Care :-
                         71.Shampoos    ={sampo}
                         72.Conditioners={cnditnr}
                         73.Hair Oils   ={hrol}
                         
                         #:-Fragnance :-
                         74.Deos    ={deo}
                         75.Perfumes={prfm}
                         76.Roll Ons={rol} ''')
                                
                if b==2:
                    print("Welcome to the Stock Management Panel")
                    print(f'''
                           1. HP    (Thin and Light Laptop)       ={hp}
                           2. Dell  (Ultra Light Weight)          ={dell} 
                           3. Apple (Ultra Light and Long Lasting)={apple}
                           4. Boat    (Bluetooth Headset)           ={boath}
                           5. Samsung (Truly Wireless Headphones)   ={samh}
                           6. Realme  (Silicon Neckband and Earwing)={realmeh}
                           7. Canon (Sports and Action Camera)={canon}
                           8. Sony  (Perfect for Beginners)   ={sony}
                           9. Nikon (Digital Zoom Camera)     ={nikon}
                           10. Iphone  (ios 14)           ={iphn}
                           11. Samsung (Android 11)       ={sams}
                           12. Oneplus (5g Phone)         ={onepls}
                           13. Straightner (Nova Smooth)={strner}
                           14. Trimmer (Chargable)      ={trimr}
                           15. Curler (Electric Curler) ={cler}
                           16. Shirt (Small Size)   ={sirts}
                           17.Shirt (Medium Size)  ={sirtm}
                           18.Shirt (Large Size)   ={sirtl}
                           19.T-Shirt (Small Size) ={tsirts}
                           20.T-Shirt (Medium Size)={tsirtm}
                           21.T-Shirt (Large Size) ={tsirtl}
                           22.Jeans (Small Size)   ={jens}
                           23.Jeans (Medium Size)  ={jenm}
                           24.Jeans  ( Large Size) ={jenl}
                           25.Casual (Small Size)   ={cass}
                           26.Casual (Medium Size)  ={casm}
                           27.Casual (Large Size)   ={casl}
                           28.Formal (Small Size)   ={forms}
                           29.Formal (Medium Size)  ={formm}
                           30.Formal (Large Size)   ={forml}
                           31.Slippers (Small Size) ={slips}
                           32.Slippers (Medium Size)={slipm}
                           33.Slippers (Large Size) ={slipl}
                           34.Kurta (Small Size)         ={kurws}
                           35.Kurta (Medium Size)        ={kurwm}
                           36.Kurta (Large Size)         ={kurwl}
                           37.Saree (Shiny and Silk Made)={sare}
                           38.Girls Tops (Small Size)    ={tops}
                           39.Girls Tops (Medium Size)   ={topm}
                           40.Girls Tops (Large Size)    ={topl}
                           41.Shoes (Small Size Women Shoes)   ={shoes}
                           42.Shoes (Medium Size Women Shoes)  ={shoem}
                           43.Shoes (Large Size Women Shoes)   ={shoel}
                           44.Heels (Small Size Women Heels)   ={heels}
                           45.Heels (Medium Size Women Heels)  ={heelm}
                           46.Heels (Large Size Women Heels)   ={heell}
                           47.Sandle (Small Size Women Sandle) ={sandls}
                           48.Sandle (Medium Size Women Sandle)={sandlm}
                           49.Sandle (Large Size Women Sandle) ={sandll}
                           50.Dress (Small Size Dress For kids)  ={dres}
                           51.Dress (Medium Size Dress for kids) ={drem}
                           52.Dress (Large Size Dress for kids)  ={drel}
                           53.Jeans (Small Size Jeans for Kids)  ={js}
                           54.Jeans (Medium Size Jeans for Kids) ={jm}
                           55.Jeans (Large Size Jeans for Kids)  ={jl}
                           56.Ethnic Wears (Small Size for Kids) ={ews}
                           57.Ethnic Wears (Medium Size for Kids)={ewm}
                           58.Ethnic Wears (Large Size for Kids) ={ewl}
                           59.Shoes (Small Size Shoes For Kids)       ={shks}
                           60.Shoes (Medium Size Shoes For Kids)      ={shkm}
                           61.Shoes (Large Size Shoes For Kids)       ={shkl}
                           62.Sandals (Small Size Sandals For Kids)   ={sandks}
                           63.Sandals (Medium Size Sandals For Kids)  ={sandkm}
                           64.Sandals (Large Size Sandals For Kids)   ={sandkl}
                           65.Slippers (Small Size Slippers for Kids) ={slipks}
                           66.Slippers (Medium Size Slippers for Kids)={slipkm}                                                 
                           67.Slippers (Large Size Slippers for Kids) ={slipkl}
                           68.Serum   ={serum}
                           69.Facewash={facwas}
                           70.Lotion  ={lotn}
                           71.Shampoos    ={sampo}
                           72.Conditioners={cnditnr}
                           73.Hair Oils   ={hrol}                        
                           74.Deos    ={deo}
                           75.Perfumes={prfm}
                           76.Roll Ons={rol} ''')
                    print("**Enter the serial number of item whose amount you want to change**")
                    e='Y'
                    while(e=='Y'):
                            f=int(input())
                            print("Enter the New Amount of Item")
                            if f==1:
                                sirts=input()
                            if f==2:
                               sirtm=input()
                            if f==3:
                                sirtl=input()
                            if f==4:
                                tsirts=input()
                            if f==5:
                                tsirtm=input()
                            if f==6:
                                tsirtl=input()
                            if f==7:
                                jens=input()
                            if f==8:
                                jenm=input()
                            if f==9:
                                jenl=input()
                            if f==10:
                                iphn=input()
                            if f==11:
                               sams=input()
                            if f==12:
                                onepls=input()
                            if f==13:
                                strner=input()
                            if f==14:
                                trimr=input()
                            if f==15:
                                cler=input()
                            if f==16:
                                sirts=input()
                            if f==17:
                                sirtm=input()
                            if f==18:
                                sirtl=input()
                            if f==19:
                                tsirts=input()
                            if f==20:
                               tsirtm=input()
                            if f==21:
                                tsirtl=input()
                            if f==22:
                                jens=input()
                            if f==23:
                                jenm=input()
                            if f==24:
                                jenl=input()
                            if f==25:
                                cass=input()
                            if f==26:
                                casm=input()
                            if f==27:
                                casl=input()
                            if f==28:
                                forms=input()
                            if f==29:
                               formm=input()
                            if f==30:
                                forml=input()
                            if f==31:
                                slips=input()
                            if f==32:
                                slipm=input()
                            if f==33:
                                slipl=input()
                            if f==34:
                                kurws=input()
                            if f==35:
                                kurwm=input()
                            if f==36:
                                kurwl=input()
                            if f==37:
                                sare=input()
                            if f==38:
                               tops=input()
                            if f==39:
                                topm=input()
                            if f==40:
                                topl=input()
                            if f==41:
                                shoes=input()
                            if f==42:
                                shoem=input()
                            if f==43:
                                shoel=input()
                            if f==44:
                                heels=input()
                            if f==45:
                                heelm=input()
                            if f==46:
                                heell=input()
                            if f==47:
                               sandls=input()
                            if f==48:
                                sandlm=input()
                            if f==49:
                                sandll=input()
                            if f==50:
                                dres=input()
                            if f==51:
                                drem=input()
                            if f==52:
                                drel=input()
                            if f==53:
                               js=input()
                            if f==54:
                                jm=input()
                            if f==55:
                                jl=input()
                            if f==56:
                                ews=input()
                            if f==57:
                                ewm=input()
                            if f==58:
                                ewl=input()
                            if f==59:
                                shks=input()
                            if f==60:
                                shkm=input()
                            if f==61:
                                shkl=input()
                            if f==62:
                               sandks=input()
                            if f==63:
                                sandkm=input()
                            if f==64:
                                sandkl=input()
                            if f==65:
                                slipks=input()
                            if f==66:
                                slipkm=input()
                            if f==67:
                                slipkl=input()
                            if f==68:
                                serum=input()
                            if f==69:
                                facwas=input()
                            if f==70:
                                lotn=input()
                            if f==71:
                               sampo=input()
                            if f==72:
                                cnditnr=input()
                            if f==73:
                                hrol=input()
                            if f==74:
                                deo=input()
                            if f==75:
                                prfm=input()
                            if f==76:
                                rol=input()
                            print("If you want to continue Press Y else Press N")
                            e=input()
                            if e=='N':
                                break
                            elif (e!='Y' and e!='N'):
                                print("Enter valid choice")
                    print("New Stock of Items After Updation  ")
                    print(f'''
                           1. HP    (Thin and Light Laptop)       ={hp}
                           2. Dell  (Ultra Light Weight)          ={dell} 
                           3. Apple (Ultra Light and Long Lasting)={apple}
                           4. Boat    (Bluetooth Headset)           ={boath}
                           5. Samsung (Truly Wireless Headphones)   ={samh}
                           6. Realme  (Silicon Neckband and Earwing)={realmeh}
                           7. Canon (Sports and Action Camera)={canon}
                           8. Sony  (Perfect for Beginners)   ={sony}
                           9. Nikon (Digital Zoom Camera)     ={nikon}
                           10. Iphone  (ios 14)           ={iphn}
                           11. Samsung (Android 11)       ={sams}
                           12. Oneplus (5g Phone)         ={onepls}
                           13. Straightner (Nova Smooth)={strner}
                           14. Trimmer (Chargable)      ={trimr}
                           15. Curler (Electric Curler) ={cler}
                           16. Shirt (Small Size)   ={sirts}
                           17.Shirt (Medium Size)  ={sirtm}
                           18.Shirt (Large Size)   ={sirtl}
                           19.T-Shirt (Small Size) ={tsirts}
                           20.T-Shirt (Medium Size)={tsirtm}
                           21.T-Shirt (Large Size) ={tsirtl}
                           22.Jeans (Small Size)   ={jens}
                           23.Jeans (Medium Size)  ={jenm}
                           24.Jeans  ( Large Size) ={jenl}
                           25.Casual (Small Size)   ={cass}
                           26.Casual (Medium Size)  ={casm}
                           27.Casual (Large Size)   ={casl}
                           28.Formal (Small Size)   ={forms}
                           29.Formal (Medium Size)  ={formm}
                           30.Formal (Large Size)   ={forml}
                           31.Slippers (Small Size) ={slips}
                           32.Slippers (Medium Size)={slipm}
                           33.Slippers (Large Size) ={slipl}
                           34.Kurta (Small Size)         ={kurws}
                           35.Kurta (Medium Size)        ={kurwm}
                           36.Kurta (Large Size)         ={kurwl}
                           37.Saree (Shiny and Silk Made)={sare}
                           38.Girls Tops (Small Size)    ={tops}
                           39.Girls Tops (Medium Size)   ={topm}
                           40.Girls Tops (Large Size)    ={topl}
                           41.Shoes (Small Size Women Shoes)   ={shoes}
                           42.Shoes (Medium Size Women Shoes)  ={shoem}
                           43.Shoes (Large Size Women Shoes)   ={shoel}
                           44.Heels (Small Size Women Heels)   ={heels}
                           45.Heels (Medium Size Women Heels)  ={heelm}
                           46.Heels (Large Size Women Heels)   ={heell}
                           47.Sandle (Small Size Women Sandle) ={sandls}
                           48.Sandle (Medium Size Women Sandle)={sandlm}
                           49.Sandle (Large Size Women Sandle) ={sandll}
                           50.Dress (Small Size Dress For kids)  ={dres}
                           51.Dress (Medium Size Dress for kids) ={drem}
                           52.Dress (Large Size Dress for kids)  ={drel}
                           53.Jeans (Small Size Jeans for Kids)  ={js}
                           54.Jeans (Medium Size Jeans for Kids) ={jm}
                           55.Jeans (Large Size Jeans for Kids)  ={jl}
                           56.Ethnic Wears (Small Size for Kids) ={ews}
                           57.Ethnic Wears (Medium Size for Kids)={ewm}
                           58.Ethnic Wears (Large Size for Kids) ={ewl}
                           59.Shoes (Small Size Shoes For Kids)       ={shks}
                           60.Shoes (Medium Size Shoes For Kids)      ={shkm}
                           61.Shoes (Large Size Shoes For Kids)       ={shkl}
                           62.Sandals (Small Size Sandals For Kids)   ={sandks}
                           63.Sandals (Medium Size Sandals For Kids)  ={sandkm}
                           64.Sandals (Large Size Sandals For Kids)   ={sandkl}
                           65.Slippers (Small Size Slippers for Kids) ={slipks}
                           66.Slippers (Medium Size Slippers for Kids)={slipkm}                                                 
                           67.Slippers (Large Size Slippers for Kids) ={slipkl}
                           68.Serum   ={serum}
                           69.Facewash={facwas}
                           70.Lotion  ={lotn}
                           71.Shampoos    ={sampo}
                           72.Conditioners={cnditnr}
                           73.Hair Oils   ={hrol}                        
                           74.Deos    ={deo}
                           75.Perfumes={prfm}
                           76.Roll Ons={rol} ''')
                      
            else:
                print("Please Enter the Valid Passward")
        else:
            print("Please,Enter the Valid ID")
            
    elif a=='B':
        print("Welcome to the shopping app ")
        print("                     ***Hello Shopper*** \n\n    ")
        print("                     Here is the dashboard       ")
        print("                      Choose the catergory    \n")
        print(f''' 
                                         1.ELECTRONICS ITEMS
                                         2.FASHION
                                         3.BEAUTY
                        ''')
        caty=int(input("Enter your choice-"))
                
        if(caty==1):
                    print(f'''   
                              LAPTOPS:-      ITEM                                RATINGS
                                             
                                         1.HP --> MRP Rs.50,000                  ***
                                           Description--
                                 Light weight,6-7 hours lasting battery,
                                 64 GB RAM
                                                
                                         2.DELL --> MRP Rs.55,000                ****
                                            Description--
                                 Light weight,10 hours lasting battery,
                                 128 GB RAM
                                                
                                         3.MAC BOOK --> MRP Rs.1,08,900          *****
                                            Description--
                                 Very Light weight, long lasting battery upto 
                                 12 hours,
                                 256 GB RAM
                ______________________________________________________________________________
                    
                    HEADPHONES:-             ITEM                                RATINGS
                                                
                                         4.BOAT  --> MRP 2,999                   ****
                                           Description--
                                     10 hours playback time, 1 year warranty,
                                     truly Wireless
                                     10m range
                                                
                                         5.SAMSUNG  --> MRP 3,500                *****
                                           Description--
                                     12 hours playback time, 1 year warranty,
                                     Wireless,2 hours full Charge 
                                     12m range
                                                
                                         6.REALME   --> MRP 2,299                ***
                                           Description--
                                     8-10 hours playback time, 1 year warranty,
                                     Wireless, 3-4 hours full Charge            
                _________________________________________________________________________________
                    
                    CAMERAS:-                   ITEM                             RATINGS
                                                    
                                         7.CANON --> MRP Rs.50,000               ****
                                           Description--
                                         50D lens, handy, black colour with
                                         autofocus of 9 points
                                         
                                         8.SONY  --> MRP Rs.36,950               ****
                                           Description--
                                         65D lens, handy, grey black, autofocus
                                         of 7 points
                                            
                                         9.NIKON  --> MRP Rs.71,000              *****
                                           Description--
                                         30D lens, charcoal black, autofocus of
                                         13 points
                ___________________________________________________________________________________
                    
                    MOBILE PHONES:-          ITEM                                RATINGS
                                                
                                         10.IPHONE --> MRP Rs.70,000             *****
                                           Description--
                                         IOS 14, Midnight Blue, 128 GB,
                                         Water Resistance
                                            
                                         11.SAMSUNG --> MRP Rs.34,000            ****
                                           Description--
                                         Android 14, 48 megapixels front Camera,
                                         4300mAh,sky blue
                                         
                                         12.ONEPLUS--> MRP Rs.34,000             *****
                                           Description--
                                         Alexa inbuilt, Oxygen OS, 6.62 inches
                                         display, 50MP main Camera
                ____________________________________________________________________________________                       
                 
                    STYLING GADGETS              ITEM                            RATINGS
                                                
                                         13. STRAIGHTNER--> MRP Rs.5,000         ***
                                           Description--
                                         Light weight, handy, 2 years warranty
                                            
                                         14.CURLER--> MRP Rs.3,000               ****
                                            Description--
                                         Ceramic, 2 in 1(curler and crimper)
                                         shine adding qualities
                                            
                                         15.TRIMMER--> MRP Rs.3,500              *****
                                            Description--
                                         Fast Charge,6-7 hours lasting battery,
                                         no cut gurantee
                                            ''')
                    print("LOGIN TO CONTINUE SHOPPING!!!!")                            
                    
        elif(caty==2):
                    print(f'''         
                             1.MEN----                
                             
                            CLOTHING                 ITEM                        RATINGS
                                                     
                                                     16.SHIRT--MRP Rs.500        *** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Black, Blue, Green, Grey colours are
                                         available, 100% cotton, easily washable
                                                        
                                                     17.TSHIRT--MRP Rs.550       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Pink, White, Red colours are available
                                         100% pure fabric
                                                        
                                                     18.JEANS--MRP Rs.1000       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Dark Blue, Light Blue, White, Black
                                         are available, 100% denim, easily 
                                         washable
                                             
                            FOOTWEAR                  ITEM                       RATINGS
                                                        
                                                     19.SLIPPERS--MRP Rs.200     ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Comfortable and lightwear, Rubber,
                                         Water Resistance, Flat 
                                                        
                                                     20.SANDALS--MRP Rs.500      ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Rubber Lightweight Sandal for men,
                                         Brown, Black, Coffee colours are 
                                         available
                                                     
                                                     21.SHOES--MRP Rs.4500       ***
                                             SIZES AVAILABLE-- S,M,L  
                                             Description--
                                         Sports Shoes with Sole for Jumping and
                                         Running
                            ________________________________________________________________________________________                         
                                    
                            2.WOMEN----
                                
                            CLOTHING                ITEM                         RATINGS
                                                    
                                                     22.KURTA--MRP Rs800         ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Emboridered Solid Cotton Straight Fit 
                                         Kurta 
                                                        
                                                     23.SAREE--MRP Rs.4000       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Pure Georgette with Blouse Piece,
                                         Purple, Mehroon, Baby Pink 
                                                     
                                                     24.TOPS--MRP Rs.500         ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Stylish, Comfortable, Crop Top 
                                         
                             FOOTWEAR           ITEM                             RATINGS
                                                     
                                                     25.HEELS--MRP Rs2500        ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         4 inches pencil heel, black and brown 
                                         colours are available
                                                    
                                                     26.SHOE--MRP Rs.4500        ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         leather sole, comfortable, black in 
                                         colour
                                                     
                                                     27.SANDALS--MRP Rs.1500     ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         flats, thermoplastic rubber,comfortable
                                         to walk
                       ________________________________________________________________________________________                         
                                 
                            3.CHILDREN 
                                
                            CLOTHING         ITEM                                RATINGS
                                                        
                                                     28.DRESSES--MRP Rs.500      **** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--comfortable,trendy
                             
                             
                                                     29.ETHNIC WEAR--MRP Rs.750  ***
                                             SIZES AVAILABLE-- S,M,L
                                             Description--fashionable,cotton based
                             
                             
                                                     30.JEANS--MRP Rs.1300       ***** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description-- strechable,breathable material
                             
                             
                             
                                       
                            FOOTWEAR             ITEM                            RATINGS
                            
                            
                             
                             
                                     31.SLIPPERS--MRP Rs.500                                   ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION-soft,comfortable
                             
                                                            
                                     32.SANDALS--MRP Rs.500                                    ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION--trendy,party wear
                             
                             
                                     33.SHOES--MRP Rs.1000                                      ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION--light sole,leather based       
                            
                            ''')
                    print("LOGIN TO CONTINUE SHOPPING!!!!")           
        elif(caty==3):
                    print(f'''
                                1.SKINCARE     
                                                         ITEM                          RATINGS
                                                         
                                                    34.SERUMS-->MRP Rs.200
                                                    Description--skin friendly,          ***
                                                    pareben free
                                                    
                                                    
                                                    
                                                    35.FACEWASH-->MRP Rs.200
                                                    Description--skin friendly,          ***
                                                    pareben free
                                                    
                                                    
                                                    36.LOTION-->MRP Rs.400
                                                    Description--skin friendly,          ***
                                                    pareben free
                         ________________________________________________________________________________________                         
                            
                                2.HAIRCARE              
                                                        ITEM                          RATINGS
                                                        
                                                        
                                                     37.SHAMPOO-->MRP Rs.200
                                                     Description--hair friendly,          ***
                                                    pareben free
                                                     
                                                     
                                                     
                                                     38.HAIRCONDITIONER-->MRP Rs.500
                                                     Description--hair friendly,          ***
                                                    works for 10 hours
                                                
                                                
                                                     39.HAIR OILS-->MRP Rs.250
                                                     Description--skin friendly,          ***
                                                    pareben free
                                                
                                3.FRAGRANCE
                                                         ITEM                           RATINGS
                                         
                                                         40.DEOS-->MRP Rs.750
                                                         Description--skin friendly,      ***
                                                        long lasting
                                                         
                                                         
                                                         
                                                         41.ROLL-ONS-->MRP Rs.500
                                                         Description--skin friendly,
                                                         long lasting                      ***
                                                   
                                                         
                                                         
                                                         42.PERFUMES-->MRP Rs.1000
                                                         Description--skin friendly,
                                                         long lasting                      ***
                                            
                                                            ''')
                    print("LOGIN TO CONTINUE SHOPPING!!!!")   
                   
    elif a=='N':
        print("Thanks for using the App")
        
        break
    elif a=='U':
        print("welcome to the user panel")
        print("Enter your user ID-")
        uid=input()
        uid=uid.lower()
        if(uid==u1 or uid==u2 or uid==u3):
            upss=input("Enter your password ")
            if((uid==u1 and upss==p1)or(uid==u2 and upss==p2 )or(uid==u3 and upss==p3)):
                print("sucessfully loged-in  into the user panel")
                print("Welcome to the shopping app ")
                print("                     ***Hello Shopper*** \n\n    ")
                print("                     Here is the dashboard       ")
                print("                      Choose the catergory    \n")
                print(f''' 
                                         1.ELECTRONICS ITEMS
                                         2.FASHION
                                         3.BEAUTY
                        ''')
                caty=int(input("Enter your choice-"))
                
                if(caty==1):
                    
                    print(f'''   
                              LAPTOPS:-      ITEM                                RATINGS
                                             
                                         1.HP --> MRP Rs.50,000                  ***
                                           Description--
                                 Light weight,6-7 hours lasting battery,
                                 64 GB RAM
                                                
                                         2.DELL --> MRP Rs.55,000                ****
                                            Description--
                                 Light weight,10 hours lasting battery,
                                 128 GB RAM
                                                
                                         3.MAC BOOK --> MRP Rs.1,08,900          *****
                                            Description--
                                 Very Light weight, long lasting battery upto 
                                 12 hours,
                                 256 GB RAM
                ______________________________________________________________________________
                    
                    HEADPHONES:-             ITEM                                RATINGS
                                                
                                         4.BOAT  --> MRP 2,999                   ****
                                           Description--
                                     10 hours playback time, 1 year warranty,
                                     truly Wireless
                                     10m range
                                                
                                         5.SAMSUNG  --> MRP 3,500                *****
                                           Description--
                                     12 hours playback time, 1 year warranty,
                                     Wireless,2 hours full Charge 
                                     12m range
                                                
                                         6.REALME   --> MRP 2,299                ***
                                           Description--
                                     8-10 hours playback time, 1 year warranty,
                                     Wireless, 3-4 hours full Charge            
                _________________________________________________________________________________
                    
                    CAMERAS:-                   ITEM                             RATINGS
                                                    
                                         7.CANON --> MRP Rs.50,000               ****
                                           Description--
                                         50D lens, handy, black colour with
                                         autofocus of 9 points
                                         
                                         8.SONY  --> MRP Rs.36,950               ****
                                           Description--
                                         65D lens, handy, grey black, autofocus
                                         of 7 points
                                            
                                         9.NIKON  --> MRP Rs.71,000              *****
                                           Description--
                                         30D lens, charcoal black, autofocus of
                                         13 points
                ___________________________________________________________________________________
                    
                    MOBILE PHONES:-          ITEM                                RATINGS
                                                
                                         10.IPHONE --> MRP Rs.70,000             *****
                                           Description--
                                         IOS 14, Midnight Blue, 128 GB,
                                         Water Resistance
                                            
                                         11.SAMSUNG --> MRP Rs.34,000            ****
                                           Description--
                                         Android 14, 48 megapixels front Camera,
                                         4300mAh,sky blue
                                         
                                         12.ONEPLUS--> MRP Rs.34,000             *****
                                           Description--
                                         Alexa inbuilt, Oxygen OS, 6.62 inches
                                         display, 50MP main Camera
                ____________________________________________________________________________________                       
                 
                    STYLING GADGETS              ITEM                            RATINGS
                                                
                                         13. STRAIGHTNER--> MRP Rs.5,000         ***
                                           Description--
                                         Light weight, handy, 2 years warranty
                                            
                                         14.CURLER--> MRP Rs.3,000               ****
                                            Description--
                                         Ceramic, 2 in 1(curler and crimper)
                                         shine adding qualities
                                            
                                         15.TRIMMER--> MRP Rs.3,500              *****
                                            Description--
                                         Fast Charge,6-7 hours lasting battery,
                                         no cut gurantee
                                            ''')
                    electro={1:50000,2:55000,3:108900,4:2999,5:3500,6:2299,7:50000,8:36950,9:71000,10:70000,11:34000,12:34000,13:5000,14:3000,15:3500}
                    sum=0
                    want='Y'
                    while(want=='Y'):
                        print("Enter the number that you want- ")
                        ele=int(input())
                        q=int(input("Enter the quantity-"))
                        sum=sum+electro[ele]*q
                        want=input("Enter Y to continue and any other key to discontinue ")
                        want=want.upper()
                    print(f"Your total is {sum}") 
                    print("PLACE ORDER")
                    name=input("Enter your name-")
                    addr=input("Enter your address-")
                    con=input("Enter your mobile number-")
                    print(f"Your bill is {sum}\n To view discounts on your purchase press D else press B  to view the bill ")
                    dis=input()
                    dis=dis.upper()
                    if dis=="D":
                        if (sum<15000 and sum >10000) :
                            print("You get a 5% off!!")
                            sum=sum-0.05*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum<30000 and sum>=15000) :
                            print("You get a 15% off!!")
                            sum=sum-0.15*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28  April''')
                            print("Thanks for shopping")
                        elif (sum<50000 and sum>=30000) :
                            print("You get a 25% off!!")
                            sum=sum-0.25*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum>=50000) :
                            print("You get a 45% off!!")
                            sum=sum-0.45*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28  April''')
                            print("Thanks for shopping")
                        else :
                            print(f'''Buy above 10000 and get your discount\nHI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28 April' ''')
                    elif dis=="B":
                        print(f'''HI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28  April''')
                        print("Thanks for shopping")
                        
                elif(caty==2):
                    print(f'''         
                             1.MEN----                
                             
                            CLOTHING                 ITEM                        RATINGS
                                                     
                                                     16.SHIRT--MRP Rs.500        *** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Black, Blue, Green, Grey colours are
                                         available, 100% cotton, easily washable
                                                        
                                                     17.TSHIRT--MRP Rs.550       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Pink, White, Red colours are available
                                         100% pure fabric
                                                        
                                                     18.JEANS--MRP Rs.1000       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Dark Blue, Light Blue, White, Black
                                         are available, 100% denim, easily 
                                         washable
                                             
                            FOOTWEAR                  ITEM                       RATINGS
                                                        
                                                     19.SLIPPERS--MRP Rs.200     ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Comfortable and lightwear, Rubber,
                                         Water Resistance, Flat 
                                                        
                                                     20.SANDALS--MRP Rs.500      ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Rubber Lightweight Sandal for men,
                                         Brown, Black, Coffee colours are 
                                         available
                                                     
                                                     21.SHOES--MRP Rs.4500       ***
                                             SIZES AVAILABLE-- S,M,L  
                                             Description--
                                         Sports Shoes with Sole for Jumping and
                                         Running
                            ________________________________________________________________________________________                         
                                    
                            2.WOMEN----
                                
                            CLOTHING                ITEM                         RATINGS
                                                    
                                                     22.KURTA--MRP Rs800         ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Emboridered Solid Cotton Straight Fit 
                                         Kurta 
                                                        
                                                     23.SAREE--MRP Rs.4000       ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Pure Georgette with Blouse Piece,
                                         Purple, Mehroon, Baby Pink 
                                                     
                                                     24.TOPS--MRP Rs.500         ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         Stylish, Comfortable, Crop Top 
                                         
                             FOOTWEAR           ITEM                             RATINGS
                                                     
                                                     25.HEELS--MRP Rs2500        ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         4 inches pencil heel, black and brown 
                                         colours are available
                                                    
                                                     26.SHOE--MRP Rs.4500        ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         leather sole, comfortable, black in 
                                         colour
                                                     
                                                     27.SANDALS--MRP Rs.1500     ** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--
                                         flats, thermoplastic rubber,comfortable
                                         to walk
                       ________________________________________________________________________________________                         
                                 
                            3.CHILDREN 
                                
                            CLOTHING         ITEM                                RATINGS
                                                        
                                                     28.DRESSES--MRP Rs.500      **** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--comfortable,trendy
                             
                             
                                                     29.ETHNIC WEAR--MRP Rs.750  ***
                                             SIZES AVAILABLE-- S,M,L
                                             Description--comfortable,trendy
                             
                             
                                                     30.JEANS--MRP Rs.1300       ***** 
                                             SIZES AVAILABLE-- S,M,L
                                             Description--strechable,
                                             breathable material
                             
                             
                             
                                       
                            FOOTWEAR             ITEM                            RATINGS
                            
                            
                             
                             
                                     31.SLIPPERS--MRP Rs.500                                   ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION-soft and comfortable
                             
                                                            
                                     32.SANDALS--MRP Rs.500                                    ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION--trendy,party wear
                             
                             
                                     33.SHOES--MRP Rs.1000                                      ** 
                             SIZES AVAILABLE-- S,M,L
                             DESCRIPTION--light sole,leather based        
                            
                            ''')
                    fashion={16:500,17:550,18:1000,19:200,20:500,21:4500,22:800,23:4000,24:500,25:2500,26:4500,27:1500,28:500,29:2500,30:1500,31:500,32:500,33:1000} 
                    sum=0
                    want='Y'
                    while(want=='Y'):
                        print("Enter the number that you want- ")
                        ele=int(input())
                        q=int(input("Enter the quantity-"))
                        sum=sum+fashion[ele]*q
                        want=input("Enter Y to continue and any other key to discontinue ")
                        want=want.upper()
                    print(f"Your total is {sum}") 
                    print("PLACE ORDER")
                    name=input("Enter your name-")
                    addr=input("Enter your address-")
                    con=input("Enter your mobile number-")
                    print(f'''Your bill is {sum}\n To view discounts on your purchase press D else press B  to view the bill ''')
                    dis=input()
                    dis=dis.upper()
                    if dis=="D":
                        if (sum<15000 and sum >10000) :
                            print("You get a 5% off!!")
                            sum=sum-0.05*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum<30000 and sum>=15000) :
                            print("You get a 15% off!!")
                            sum=sum-0.15*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum<50000 and sum>=30000) :
                            print("You get a 25% off!!")
                            sum=sum-0.25*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum>=50000) :
                            print("You get a 45% off!!")
                            sum=sum-0.45*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''') 
                            print("Thanks for shopping")
                        else :
                            print(f'''Buy above 10000 and get your discount\nHI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28 March ''')
                    elif dis=="B":
                        print(f'''HI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28  April''')
                        print("Thanks for shopping")
                    
                elif(caty==3):
                    
                    print(f'''
                                1.SKINCARE     
                                                         ITEM                        RATINGS
                                                         
                                                    34.SERUMS-->MRP Rs.200
                                                    Description--skin friendly,          ***
                                                    paraben free
                                                    
                                                    
                                                    
                                                    35.FACEWASH-->MRP Rs.200
                                                    Description--skin friendly,          ***
                                                    paraben free
                                                    
                                                    
                                                    36.LOTION-->MRP Rs.400
                                                    Description--skin friendly,          ***
                                                    paraben free
                         ________________________________________________________________________________________                         
                            
                                2.HAIRCARE              
                                                        ITEM                        RATINGS
                                                        
                                                        
                                                     37.SHAMPOO-->MRP Rs.200
                                                     Description--hair friendly,          ***
                                                    paraben free
                                                     
                                                     
                                                     
                                                    38.HAIRCONDITIONER-->MRP Rs.500
                                                    Description--hair friendly,          ***
                                                    works for 10 hours
                                                
                                                    
                                                    39.HAIR OILS-->MRP Rs.250
                                                    Description--skin friendly,          ***
                                                    paraben free
                                                
                                3.FRAGRANCE
                                                         ITEM                        RATINGS
                                         
                                                         40.DEOS-->MRP Rs.750
                                                         Description--skin friendly,
                                                         long lasting                      ***
                                                   
                                                         
                                                         
                                                         
                                                         41.ROLL-ONS-->MRP Rs.500
                                                         Description--skin friendly,
                                                         long lasting                      ***
                                                   
                                                         
                                                         
                                                         42.PERFUMES-->MRP Rs.1000
                                                         Description--skin friendly,
                                                         long lasting                      ***
                                                            ''')
                    beauty={34:200,35:200,36:400,37:200,38:500,39:250,40:750,41:500,42:1000}
                    sum=0
                    want='Y'
                    while(want=='Y'):
                        print("Enter the number that you want- ")
                        ele=int(input())
                        q=int(input("Enter the quantity-"))
                        sum=sum+beauty[ele]*q
                        want=input("Enter Y to continue and any other key to discontinue ")
                        want=want.upper()
                    print(f"Your total is {sum}") 
                    print("PLACE ORDER")
                    name=input("Enter your name-")
                    addr=input("Enter your address-")
                    con=input("Enter your mobile number-")
                    print(f"Your bill is {sum}\n To view discounts on your purchase press D else press B  to view the bill ")
                    dis=input()
                    dis=dis.upper()
                    if dis=="D":
                        if (sum<15000 and sum >10000) :
                            print("You get a 5% off!!")
                            sum=sum-0.05*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28  April''')
                            print("Thanks for shopping")
                        elif (sum<30000 and sum>=15000) :
                            print("You get a 15% off!!")
                            sum=sum-0.15*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum<50000 and sum>=30000) :
                            print("You get a 25% off!!")
                            sum=sum-0.25*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        elif (sum>=50000) :
                            print("You get a 45% off!!")
                            sum=sum-0.45*sum
                            print(f'''HI {name}\nYour bill is of Rs. {sum}\nYour order will be delieverd to {addr} by 28 April''')
                            print("Thanks for shopping")
                        else :
                            print(f'''Buy above 10000 and get your discount\nHI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28 April ''')
                    elif dis=="B":
                        print(f'''HI {name},\n Your total bill is of Rs. {sum} and will be delieverd to {addr} by 28  April ''')
                        print("Thanks for shopping")
                        
                else:
                    print("Enter valid choice for shopping")
                
                
            else:
                print("Enter valid user password")
                
        else:
            print("Enter valid user ID")
        
    else:
        print("Please,Enter the Valid Choice")
        