import binascii as b

s = "8189844c408d99408485819240978194938f8e4c4094888194408d8f9394408f8640998f959240838f8e838c9593898f8e9340978592852d2a8592928f8e858f95934e409788858e40894093818984409488819440998f95409394898d958c81948584408d854089408d85818e944c40948f4082852d2a8692818e8b4c409488819440898e408e8f94898e8740998f95924086818c8c8183898593408940978193408f83838193898f8e818c8c99408795898485842d2a948f9781928493409488854094929594884e408e8f94409488819440998f954081928540858e948992858c994097928f8e8740898e40948889932d2a898e9394818e83854e40948885408d818e408993408385929481898e8c99408140838f958e9492994090928183948994898f8e85924e40818e844088852d2a97818c8b93408140878f8f84408485818c4e422d2a2d2a429488858e4089409781934092898788944e422d2a2d2a42948f409488819440859894858e944e422d2a2d2a4282959440948881944097819340818c8c4e422d2a2d2a428e8f4c408e8f4c408d99408485819240978194938f8e4c408e8f9440818c8c4d4d8299408e8f408d85818e9340818c8c4e408940978f958c842d2a939587878593944c40868f92408598818d908c854c409488819440814090928593858e948194898f8e40948f408140848f83948f92408993408d8f92852d2a8c898b858c9940948f40838f8d854086928f8d408140888f93908994818c409488818e4086928f8d40814088958e944c40818e844094888194409788858e2d2a94888540898e899489818c934047834e834e474081928540908c81838584408285868f9285409488819440888f93908994818c4094888540978f9284932d2a4783888192898e874083928f9393474096859299408e81949592818c8c994093958787859394409488858d93858c9685934e422d2a2d2a42998f95408d81994082854092898788944e422d2a2d2a429488854090928f828182898c899499408c89859340898e409488819440848992858394898f8e4e40818e844089864097854094818b85409488899340819340812d2a978f928b898e87408899908f948885938993409785408881968540814086928593884082819389934086928f8d40978889838840948f409394819294408f95922d2a838f8e939492958394898f8e408f86409488899340958e8b8e8f978e4096899389948f924e422d2a2d2a4297858c8c4c409488858e4c40939590908f93898e8740948881944047834e834e884e4740848f8593409394818e8440868f92404783888192898e872d2a83928f939340888f93908994818c4c474097888194408695929488859240898e868592858e8385"
#s = "737b763e327f8b3276777384328973868581803e32867a7386327f818586328178328b81878432758180757e87857b81808532897784771f1c7784848180778187854032897a7780327b3285737b7632867a7386328b81873285867b7f877e73867776327f77327b327f777380863e3286813274771f1c788473807d3e32867a7386327b80328081867b8079328b8187843278737e7e73757b7785327b328973853281757573857b8180737e7e8b3279877b7677761f1c8681897384768532867a7732868487867a403280818632867a7386328b818732738477327780867b84777e8b328984818079327b8032867a7b851f1c7b808586738075774032867a77327f7380327b853275778486737b807e8b3273327581878086848b3282847375867b867b818077844032738076327a771f1c89737e7d8532733279818176327677737e40341f1c1f1c34867a7780327b3289738532847b797a8640341f1c1f1c34868132867a738632778a8677808640341f1c1f1c3474878632867a73863289738532737e7e40341f1c1f1c3480813e3280813e327f8b3276777384328973868581803e3280818632737e7e3f3f748b328081327f7773808532737e7e40327b328981877e761f1c858779797785863e3278818432778a737f827e773e32867a73863273328284778577808673867b8180328681327332768175868184327b85327f8184771f1c7e7b7d777e8b3286813275817f77327884817f3273327a8185827b86737e32867a7380327884817f3273327a8780863e3273807632867a738632897a77801f1c867a77327b807b867b737e85323975407540393273847732827e737577763274777881847732867a7386327a8185827b86737e32867a773289818476851f1c39757a73847b807932758481858539328877848b328073868784737e7e8b328587797977858632867a777f85777e88778540341f1c1f1c348b8187327f738b32747732847b797a8640341f1c1f1c34867a77328284817473747b7e7b868b327e7b7785327b8032867a738632767b847775867b81804032738076327b783289773286737d7732867a7b8532738532731f1c8981847d7b8079327a8b8281867a77857b85328977327a738877327332788477857a327473857b85327884817f32897a7b757a328681328586738486328187841f1c7581808586848775867b818032817832867a7b853287807d8081898032887b857b86818440341f1c1f1c3489777e7e3e32867a77803e328587828281857b807932867a73863239754075407a40393276817785328586738076327881843239757a73847b80791f1c7584818585327a8185827b86737e3e3932897a738632788784867a7784327b8078778477807577"
#s = "838b864e428f9b4286878394429983969591904e42968a8396428f919596429188429b91979442859190858e97958b91909542998794872f2c8794949190879197955042998a8790428b4295838b8642968a8396429b91974295968b8f978e83968786428f87428b428f878390964e4296914284872f2c889483908d4e42968a8396428b90429091968b9089429b9197944288838e8e83858b8795428b429983954291858583958b9190838e8e9b4289978b8687862f2c9691998394869542968a8742969497968a504290919642968a8396429b919742839487428790968b94878e9b429994919089428b9042968a8b952f2c8b909596839085875042968a87428f8390428b954285879496838b908e9b4283428591979096949b4292948385968b968b919087945042839086428a872f2c99838e8d9542834289919186428687838e50442f2c2f2c44968a8790428b4299839542948b898a9650442f2c2f2c44969142968a839642879a9687909650442f2c2f2c4484979642968a83964299839542838e8e50442f2c2f2c4490914e4290914e428f9b4286878394429983969591904e4290919642838e8e4f4f849b429091428f8783909542838e8e50428b429991978e862f2c959789898795964e4288919442879a838f928e874e42968a83964283429294879587909683968b9190429691428342869185969194428b95428f9194872f2c8e8b8d878e9b4296914285918f87428894918f4283428a9195928b96838e42968a8390428894918f4283428a9790964e4283908642968a839642998a87902f2c968a87428b908b968b838e95424985508550494283948742928e838587864284878891948742968a8396428a9195928b96838e42968a874299919486952f2c49858a83948b908942859491959549429887949b429083969794838e8e9b429597898987959642968a878f95878e98879550442f2c2f2c449b9197428f839b42848742948b898a9650442f2c2f2c44968a87429294918483848b8e8b969b428e8b8795428b9042968a839642868b948785968b91905042839086428b884299874296838d8742968a8b9542839542832f2c9991948d8b9089428a9b9291968a87958b95429987428a839887428342889487958a428483958b95428894918f42998a8b858a429691429596839496429197942f2c8591909596949785968b919042918842968a8b954297908d9091999042988b958b96919450442f2c2f2c4499878e8e4e42968a87904e429597929291958b908942968a83964249855085508a50494286918795429596839086428891944249858a83948b90892f2c8594919595428a9195928b96838e4e4942998a839642889794968a8794428b9088879487908587"
result = ''

for i in range (1,len(s),2):
    new = s[i-1:i+1]
    number = int(new,16)
    result = result + chr(number-32)
    print (number)
print (result)