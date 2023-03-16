 
from unittest import result
from colorama import Cursor
from flask import Flask, render_template,flash,redirect,url_for,session,logging,request,jsonify,json 
from flask_mysqldb import MySQL,MySQLdb
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,IntegerField,DateField,DateTimeField,DateTimeLocalField,SelectField
from passlib.hash import sha256_crypt
from functools import wraps

#Kullanıcı Giriş Decorator'ı Decoratorun içinde Session Yapısı Kullanılarak Kullanıcı Giriş Kontrolü kolayca ypılabilir
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu Sayfayı Görüntülemek İçin Giriş Yapın.","danger")
            return redirect(url_for("login"))
    return decorated_function






#Kullanıcı Kayıt Formu 
# (Wtforms avantajı flask tarafından bunu oluşturup html sayfasına göndereceğiz. Eğer html tarafında oluşturulsa her farklı form için ayrıca form yaratılması gerekecekti)

class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 3, max = 25, message= "Ad-Soyad 3-25 karakter aralığından oluşmalı" )])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5, max = 35,message= "Kullanıcı Adı 5-35 karakter aralığından oluşmalı")])
    email = StringField("Email Adresi",validators=[validators.Email(message= "Lütfen Geçerli Eposta Giriniz")])
    
    identitynumber = IntegerField("Kimlik Numarası")
    address = StringField("Adres Bilgilerinizi Giriniz",validators=[validators.Length(min = 10, max = 100, message= "Fazla Karakter Kullanıldı")])
    user_type = SelectField(u'Kullanıcı Türü', choices=[('tasıyıcı', 'Taşıyıcı'), ('tasıtan', 'Taşıtan'), ('yolcu', 'Yolcu')])

    password = PasswordField("Parola" ,validators=[
        validators.DataRequired(message = "Lütfen bir paralo belirleyin"),
        validators.EqualTo(fieldname = "confirm", message="Paralonız Uyuşmuyor")])
    confirm = PasswordField("Parola Kontrol")

class LoginForm(Form):
    username = StringField("")
    password = PasswordField("")

#Şirket Bilgileri Formu

class CompanyForm(Form):
    companyname = StringField("Şirket Adı",validators=[validators.Length(min = 1, max = 25, message= "Şirket Adı 3-25 karakter aralığından oluşmalı" )])
    companydescription = TextAreaField("Şirket Hakkında",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytypelegally = SelectField(u'Şirket Türü', choices=[('tacir', 'Tacir'), ('adisirket', 'Adi Şirket'), ('kolektifsirket', 'Kolektif Şirket'), ('komanditsirket', 'Komandit Şirket'), ('anonimsirket', 'Anonim Şirket'), ('limitedsirket', 'Limited Şirket'), ('sermayepaylıkomandit', 'Sermaye Paylı Komandit Şirket')])
    companytypefunctionally = SelectField(u'Şirket Türü', choices=[('tarımisletmeleri', 'Tarım İşletmeleri'), ('sanayiisletmeleri', 'Sanayi İşletmeleri'), ('insaatisletmeleri', 'İnşaat Sanayi ile Uğraşan İşletmeler'), ('ulastırmailetisimisletmeleri', 'Ulaştırma ve İletişim İşletmeleri'), ('finasisletmeleri', 'Finans İşletmeleri'), ('sebestdigerisletmeleri', 'Serbest Meslek ve Diğer Hizmet İşletmeleri'), ('kiralamaisletmeleri', 'Kiralama İşletmeleri')])
    companyaddress = StringField("Şirket Adresi",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companyphone = IntegerField("Şirket Telefon Numarası")
    companyemail = StringField("Şirket Email Adresi",validators=[validators.Email(message= "Lütfen Geçerli Eposta Giriniz")])
    companywebsite = StringField("Şirket Web Sitesi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companylinkedin = StringField("Şirket Linkedin Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companyfacebook = StringField("Şirket Facebook Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytwitter = StringField("Şirket Twitter Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companyinstagram = StringField("Şirket Instagram Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companyyoutube = StringField("Şirket Youtube Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companygoogleplus = StringField("Şirket Google Plus Adresi",validators=[validators.Length(min = 0, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytaxnumber = IntegerField("Şirket Vergi Numarası")
    companytaxoffice = StringField("Şirket Vergi Dairesi",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytaxadmin = StringField("Şirket Vergi Müdürü",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytaxadminphone = IntegerField("Şirket Vergi Müdürü Telefon Numarası")
    companytaxadmineposta = StringField("Şirket Vergi Müdürü Eposta Adresi",validators=[validators.Email(message= "Lütfen Geçerli Eposta Giriniz")])
    companytaxadminaddress = StringField("Şirket Vergi Müdürü Adresi",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companytaxadminidentitynumber = IntegerField("Şirket Vergi Müdürü Kimlik Numarası")
    companytaxadminidentitydate = DateField("Şirket Vergi Müdürü Kimlik Tarihi")
    companytaxadminidentityplace = StringField("Şirket Vergi Müdürü Kimlik Yeri",validators=[validators.Length(min = 5, max = 100, message= "Fazla Karakter Kullanıldı")])
    companycurrency = StringField("Şirket Para Birimi",validators=[validators.Length(min = 1, max = 25, message= "Şirket Para Birimi 3-25 karakter aralığından oluşmalı" )])



app = Flask(__name__)
#Flash mesaj yayınlanabilmesi için rastgele bir secret key olması lazım
app.secret_key= "ıtcoacs"

##### Mysql bağlantı ve konfigürasyon
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Yavrummuslera64"
app.config["MYSQL_DB"] = "itcoacs"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# Giriş Yapma Kontolüyle çalıştırmak lazım Flask Decorator(@login_required (en üstte yazılan) decorator kullan) Her oturum kontrolünde session kontrol yapsam kod uzuyordu bunun için bu decorator yardımıyla daha az kod yazılmış oldu

# 3 TİP DASHBOARD > driverdashboard, passengerdashboard, consignor(malgönderenkimse)dashboard
#Normal Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select * from tickets where ticketsowner = %s"

    result = cursor.execute(sorgu,(session["username"],))

    if result > 0:
        tickets = cursor.fetchall()
        return render_template("dashboard.html",tickets = tickets)

    else:
        return render_template("dashboard.html")

# 1. Driver Dashboard
@app.route("/driverdashboard")
@login_required
def driverdashboard():
    if session["user_type"] == 'tasıyıcı' :
            cursor = mysql.connection.cursor()
            sorgu = "Select * from tickets where ticketsowner = %s"

            result = cursor.execute(sorgu,(session["username"],))

            if result > 0:
                tickets = cursor.fetchall()
                return render_template("driverdashboard.html",tickets = tickets)

            else:
                return render_template("driverdashboard.html")
                
        # return render_template("driverdashboard.html")
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#1.1 /driverdashboard/ticketssettings 2 liste gönderilecek 1 ileri tarihli olanlar 2. geçmiş yolculuklar geçmiş yolculuklar silinemeyecek
@app.route("/driverdashboard/ticketssettings")
@login_required
def ticketssettings():
    if session["user_type"] == 'tasıyıcı' :
            cursor = mysql.connection.cursor()
            newsorgu = "Select * from tickets where ticketsowner = %s and startdate > CURRENT_DATE()"
            newresult = cursor.execute(newsorgu,(session["username"],))

            curs = mysql.connection.cursor()
            oldsorgu = "Select * from tickets where ticketsowner = %s and startdate < CURRENT_DATE()"
            oldresult = curs.execute(oldsorgu,(session["username"],))

            if newresult > 0 and oldresult == 0 :
                newtickets = cursor.fetchall()
                return render_template("ticketssettings.html",newtickets = newtickets)

            if newresult > 0 and oldresult >0:
                newtickets = cursor.fetchall()
                oldtickets = curs.fetchall()
                return render_template("ticketssettings.html",oldtickets=oldtickets,newtickets = newtickets)
            
            if newresult == 0 and oldresult > 0 :
                oldtickets = curs.fetchall()
                return render_template("ticketssettings.html",oldtickets=oldtickets)
            
            else:
                return render_template("ticketssettings.html")
                
        # return render_template("driverdashboard.html")
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

### 1.1.1 /driverdashboard/ticketssettings/cancelledtickets
@app.route("/driverdashboard/ticketssettings/cancelledticketsdriver")
@login_required
def cancelledticketsdriver():
    if session ["user_type"] == 'tasıyıcı':
        cursor = mysql.connection.cursor()
        sorgu = "Select * from cancelledticketsfrpassenger where drivername = %s"
        result = cursor.execute(sorgu,(session["username"],))

        cur = mysql.connection.cursor()
        sorgu2 = "Select * from cancelledticketsfrdriver where drivername = %s"
        result2 = cur.execute(sorgu2,(session["username"],))

        if result >0 and result2 >0 :  
            cancelledticketsfrpassenger = cursor.fetchall()
            cancelledticketsfrdriver = cur.fetchall()
            return render_template("cancelledticketsdriver.html",cancelledticketsfrpassenger=cancelledticketsfrpassenger,cancelledticketsfrdriver=cancelledticketsfrdriver)
        elif result >0 and result2 == 0:
            cancelledticketsfrpassenger = cursor.fetchall()
            return render_template("cancelledticketsdriver.html",cancelledticketsfrpassenger=cancelledticketsfrpassenger)
        elif result == 0 and result2 >0:
            cancelledticketsfrdriver = cur.fetchall()
            return render_template("cancelledticketsdriver.html",cancelledticketsfrdriver=cancelledticketsfrdriver)
            
        else:
            flash("Görüntülenecek iptal edilen sefer bulunmamaktadır","danger")
            return render_template("cancelledticketsdriver.html")
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))


### 1.2 /driverdashboard/tasıyıcı_ayar
### 1.2. /driverdashboard/tasıyıcı_ayar sayfasında tırlarım listesi, dorselerim listesi, tır-dorse ilişkisi gösterme aşamaları
@app.route("/driverdashboard/tasıyıcı_ayar")
@login_required
def  tasıyıcı_ayar ():
    
#Şuan tır ve dorseler session["username"] eşitliği üzerinden gösteriliyor fakat bunu userid üzerinden göstermemiz lazım yoksa aynı kullanıcı adı sahip farklı kullanıcıların tır ve dorseleri de o sayfada gösterilme hatası alırız.    
    #cursor = mysql.connection.cursor()
    #user_idsorgu = ("Select user_id from users where user_name = %s")
    #result = cursor.execute(user_idsorgu,(session["username"],))
    #user_id = cursor.fetchall()

    if session["user_type"] == 'tasıyıcı' :
        cursor = mysql.connection.cursor()        
        trucksorgu= "SELECT truckbrands.marka_ad, truckbrands.markaid, truckmodel.model, truckmodel.modelid, truckmodeltype.model_type_name, truckmodeltype.modeltypeid, usertruck.user_idd, usertruck.usertruck_id, usertruck.user_name, usertruck.truckbrands, usertruck.truckmodel, usertruck.truckmodeltype FROM usertruck, truckmodel, truckmodeltype, truckbrands WHERE usertruck.user_name = %s AND usertruck.truckbrands=truckbrands.markaid AND truckmodel.modelid = usertruck.truckmodel AND truckmodeltype.modeltypeid = usertruck.truckmodeltype;"
        result_truck = cursor.execute(trucksorgu,(session["username"],))
        
        cur = mysql.connection.cursor()
        trailersorgu = "SELECT trailermodel.trailermodelid , trailermodel.trailermodel_name, trailertype.trailertypeid, trailertype.trailertype_name, usertrailer.user_idd, usertrailer.user_name, usertrailer.usertrailerid, usertrailer.trailermodel_idd, usertrailer.trailertype_idd FROM usertrailer, trailermodel, trailertype WHERE usertrailer.user_name = %s AND trailermodel.trailermodelid=usertrailer.trailermodel_idd AND usertrailer.trailertype_idd = trailertype.trailertypeid;"
        result_trailer = cur.execute(trailersorgu,(session["username"],))

        if result_truck > 0 and result_trailer == 0:
            trucks = cursor.fetchall()

            return render_template("tasıyıcı_ayar.html",trucks = trucks)
        
        elif result_trailer > 0 and result_truck == 0 :
            trailer = cur.fetchall()
            return render_template("tasıyıcı_ayar.html",trailer = trailer)
        
        elif result_trailer > 0 and result_truck > 0 :
            trailer = cur.fetchall()
            trucks = cursor.fetchall()
            return render_template("tasıyıcı_ayar.html",trailer = trailer,trucks = trucks)
        
        else :
            return render_template("tasıyıcı_ayar.html")
    
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

# 1.2.2 Tır Silme Sayfası !!! Tır silme işlemini username = %s eşitliğinden değil userid = %s tarafından kurmam lazım bunu değiştirmeyi unutma
@app.route('/driverdashboard/tasıyıcı_ayar/deletetruck/<string:id>')
@login_required
def truckdelete(id) :
    if session["user_type"] == 'tasıyıcı' :
        
            cursor = mysql.connection.cursor()
            truck_usersorgusu = "SELECT * FROM usertruck WHERE user_name = %s AND usertruck_id = %s" 
            result = cursor.execute(truck_usersorgusu,(session["username"],id))
            
            if result >0 :

                truck_deletesorgu = "DELETE FROM usertruck WHERE usertruck_id = %s"

                cursor.execute(truck_deletesorgu,(id,))

                mysql.connection.commit()
                cursor.close()
                flash("Tırınız Başarıyla Silindi","success") 
                return redirect(url_for("tasıyıcı_ayar"))
            else:
                flash("Bu işlemi yapmaya yetkiniz yok.","danger")
                return redirect(url_for("tasıyıcı_ayar"))

    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))
    

# 1.2.3 Dorse Silme Sayfası
@app.route('/driverdashboard/tasıyıcı_ayar/deletetrailer/<string:id>')
@login_required
def trailerdelete(id) :
    if session["user_type"] == 'tasıyıcı' :
        
            cursor = mysql.connection.cursor()
            trailer_usersorgusu = "SELECT * FROM usertrailer WHERE user_name = %s AND usertrailerid = %s" 
            result = cursor.execute(trailer_usersorgusu,(session["username"],id))
            
            if result >0 :

                trailer_deletesorgu = "DELETE FROM usertrailer WHERE usertrailerid = %s"

                cursor.execute(trailer_deletesorgu,(id,))

                mysql.connection.commit()
                cursor.close()
                flash("Dorseniz Başarıyla Silindi","success") 
                return redirect(url_for("tasıyıcı_ayar"))
            else:
                flash("Bu işlemi yapmaya yetkiniz yok.","danger")
                return redirect(url_for("tasıyıcı_ayar"))

    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))





###### 1.2.4 Tır-Dorse İlişki Sayfası ###### session username yerine session id üzerinden devam etmek gerekiyor ilerde


@app.route('/driverdashboard/tasıyıcı_ayar/truck_trailer', methods = ["GET","POST"])
@login_required
def truck_trailermatch() :
    if session["user_type"] == 'tasıyıcı' :
        
        #ilk başta select box için verileri çektik
        cursor = mysql.connection.cursor()  
        trucksorgu= "SELECT truckbrands.marka_ad, truckbrands.markaid, truckmodel.model, truckmodel.modelid, truckmodeltype.model_type_name, truckmodeltype.modeltypeid, usertruck.user_idd, usertruck.usertruck_id, usertruck.user_name, usertruck.truckbrands, usertruck.truckmodel, usertruck.truckmodeltype FROM usertruck, truckmodel, truckmodeltype, truckbrands WHERE usertruck.user_name = %s AND usertruck.truckbrands=truckbrands.markaid AND truckmodel.modelid = usertruck.truckmodel AND truckmodeltype.modeltypeid = usertruck.truckmodeltype;"
        result_truck = cursor.execute(trucksorgu,(session["username"],))
        trucks = cursor.fetchall()

        cur = mysql.connection.cursor()
        trailersorgu = "SELECT trailermodel.trailermodelid , trailermodel.trailermodel_name, trailertype.trailertypeid, trailertype.trailertype_name, usertrailer.user_idd, usertrailer.user_name, usertrailer.usertrailerid, usertrailer.trailermodel_idd, usertrailer.trailertype_idd FROM usertrailer, trailermodel, trailertype WHERE usertrailer.user_name = %s AND trailermodel.trailermodelid=usertrailer.trailermodel_idd AND usertrailer.trailertype_idd = trailertype.trailertypeid;"
        result_trailer = cur.execute(trailersorgu,(session["username"],))
        trailer = cur.fetchall()
        
        #2. olarak önceden eşleşme yapıldıysa o verileri de çekip o sayfadaki if else bloğu içine attık
        curs = mysql.connection.cursor()
        trailertrucksorgu = "SELECT usertrucktrailer.user_name, usertrucktrailer.user_trucktrailer_id , usertrucktrailer.usertruck_id, usertrucktrailer.usertrailer_id,trailermodel.trailermodelid , trailermodel.trailermodel_name, trailertype.trailertypeid, trailertype.trailertype_name,usertrailer.trailermodel_idd, usertrailer.trailertype_idd,truckbrands.marka_ad, truckbrands.markaid, truckmodel.model, truckmodel.modelid, truckmodeltype.model_type_name, truckmodeltype.modeltypeid,usertruck.truckbrands, usertruck.truckmodel, usertruck.truckmodeltype FROM usertruck, truckmodel, truckmodeltype, truckbrands, usertrucktrailer, usertrailer, trailertype, trailermodel WHERE usertrucktrailer.user_name = %s AND usertruck.truckbrands=truckbrands.markaid AND truckmodel.modelid = usertruck.truckmodel AND truckmodeltype.modeltypeid = usertruck.truckmodeltype AND trailermodel.trailermodelid=usertrailer.trailermodel_idd AND usertrailer.trailertype_idd = trailertype.trailertypeid AND usertrucktrailer.usertrailer_id = usertrailer.usertrailerid AND usertrucktrailer.usertruck_id = usertruck.usertruck_id;"
        result_trucktrailer = curs.execute(trailertrucksorgu,(session["username"],))
        trucktrailer = curs.fetchall()

        if request.method == "POST":
            user_name = session["username"]
            usertruck_id  = request.form["usertruck_id"]
            usertrailer_id  = request.form["usertrailerid"]
            
            cursor = mysql.connection.cursor()
            sorgu = "INSERT INTO usertrucktrailer (usertruck_id,usertrailer_id,user_name) VALUES(%s,%s,%s)"
            cursor.execute(sorgu,(usertruck_id,usertrailer_id,user_name))
    
            mysql.connection.commit()
            cursor.close()




            flash("Başarıyla Tırınızda kullanacağınız dorseyi kaydettiniz. İşlere kayıt olabilirsiniz.","success")
            return redirect(url_for("tasıyıcı_ayar"))
        return render_template('truck_trailer.html',trailer = trailer,trucks = trucks, trucktrailer = trucktrailer)

    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))



#### 1.2.5 Tır-Dorse İlişkisini Silme
@app.route('/driverdashboard/tasıyıcı_ayar/deletetrucktrailer/<string:id>')
@login_required
def trucktrailerdelete(id) :
    if session["user_type"] == 'tasıyıcı' :
        
            cursor = mysql.connection.cursor()
            trucktraileruser = "SELECT * FROM usertrucktrailer WHERE user_name = %s AND user_trucktrailer_id = %s" 
            result = cursor.execute(trucktraileruser,(session["username"],id))
            
            if result >0 :

                trucktrailer_deletesorgu = "DELETE FROM usertrucktrailer WHERE user_trucktrailer_id = %s"

                cursor.execute(trucktrailer_deletesorgu,(id,))

                mysql.connection.commit()
                cursor.close()
                flash("İlişkiniz Başarıyla Silindi Yeni İlişki Kurabilirsiniz","success") 
                return redirect(url_for("tasıyıcı_ayar"))
            else:
                flash("Bu işlemi yapmaya yetkiniz yok.","danger")
                return redirect(url_for("tasıyıcı_ayar"))

    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))











### 1.2.1.1 /driverdashboard/tasıyıcı_ayar/addtruck
@app.route("/driverdashboard/tasıyıcı_ayar/addtruck" , methods = ["GET","POST"])
@login_required
def  addtruck ():
    if session["user_type"] == 'tasıyıcı':
        cursor = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result1 = cur.execute("SELECT * FROM truckbrands")
        truckbrands = cur.fetchall()

        if result1 > 0 :
            cursor = mysql.connection.cursor()
            sorgu = ("SELECT user_id FROM users WHERE username = %s")
            result = cursor.execute(sorgu,(session["username"],))
            #MySQLdb.cursors.DictCursor'dan dolayı çektiğim veriler dicte dönüştüğü için çekmek istediğim veriyi dict içerisinde it fonksiyonuyla alıp o şekilde değişkene atayıp sonrasında database tekrar atmam gerek.
            
            iddict = cursor.fetchone()
            it = iter(iddict.values())    
            user_idd = next(it)
            
            if request.method == "POST":
                user_name = session["username"]           
                truckbrands = request.form["truckbrands"]
                truckmodel  = request.form["truckmodel"]
                truckmodeltype = request.form["truckmodeltype"]
                truckyear = request.form["truckyear"]
                wheeldrive = request.form["truckyear"]
                km = request.form["km"]  
                transportcapasity = request.form["transportcapasity"]
                passengercapasity = request.form["passengercapasity"]
                wheelpercent = request.form["wheelpercent"]
                fueltype = request.form["fueltype"]
                licence_plate = request.form["licence_plate"]        
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("INSERT INTO usertruck (user_idd,user_name,truckbrands, truckmodel, truckmodeltype, truckyear,wheeldrive, km, transportcapasity, passengercapasity, wheelpercent, fueltype,licence_plate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user_idd,user_name,truckbrands,truckmodel,truckmodeltype,truckyear,wheeldrive,km,transportcapasity,passengercapasity,wheelpercent,fueltype,licence_plate))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for("tasıyıcı_ayar"))
        else: 
            pass
            
        return render_template('addtruck.html', truckbrands = truckbrands,user_idd=user_idd)
  
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

### 1.2.1.2 /driverdashboard/tasıyıcı_ayar/addtruck 
@app.route('/driverdashboard/tasıyıcı_ayar/addtruck/truckmodel/<get_truckmodel>')
@login_required
def tırmodelleri(get_truckmodel):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM truckmodel WHERE marka_id = %s", [get_truckmodel])
    truckmodel = cur.fetchall()  
    truckmodelArray = []    
    for row in truckmodel:
        truckmodelObj = {
                'modelid': row['modelid'],
                'model': row['model']}
        truckmodelArray.append(truckmodelObj)
    return jsonify({'truckmodel_brand' : truckmodelArray})

### 1.2.1.3 /driverdashboard/tasıyıcı_ayar/addtruck
@app.route('/driverdashboard/tasıyıcı_ayar/addtruck/truckmodeltype/<get_truckmodeltype>')
@login_required
def truckmodeltype(get_truckmodeltype):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM truckmodeltype WHERE model_idd = %s", [get_truckmodeltype])
    truckmodeltype = cur.fetchall()  
    truckmodeltypeArray = []
    for row in truckmodeltype:
        truckmodeltypeObj = {
                'modeltypeid': row['modeltypeid'],
                'model_type_name': row['model_type_name']}
        truckmodeltypeArray.append(truckmodeltypeObj)
    return jsonify({'truckmodeltypelist' : truckmodeltypeArray})






### 1.2.2.1 /driverdashboard/tasıyıcı_ayar/addtrailer
@app.route("/driverdashboard/tasıyıcı_ayar/addtrailer" , methods = ["GET","POST"])
@login_required
def  addtrailer ():
    if session["user_type"] == 'tasıyıcı':
        cursor = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result1 = cur.execute("SELECT * FROM trailermodel")
        trailermodel = cur.fetchall()

        if result1 > 0 :
            cursor = mysql.connection.cursor()
            sorgu = ("SELECT user_id FROM users WHERE username = %s")
            result = cursor.execute(sorgu,(session["username"],))
            #MySQLdb.cursors.DictCursor'dan dolayı çektiğim veriler dicte dönüştüğü için çekmek istediğim veriyi dict içerisinde it fonksiyonuyla alıp o şekilde değişkene atayıp sonrasında database tekrar atmam gerek.
            
            iddict = cursor.fetchone()
            it = iter(iddict.values())    
            user_idd = next(it)
            
            if request.method == "POST":
                user_name = session["username"]           
                trailermodel = request.form["trailermodel"]
                trailertype  = request.form["trailertype"]
                traileryear = request.form["traileryear"]
                wheelamount = request.form["wheelamount"]
                km = request.form["km"]  
                trailercapasity = request.form["trailercapasity"]
                wheelpercent = request.form["wheelpercent"]
                
                       
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("INSERT INTO usertrailer (user_idd,user_name,trailermodel_idd, trailertype_idd, traileryear, wheelamount, km, trailercapasity, wheelpercent ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user_idd,user_name,trailermodel,trailertype,traileryear,wheelamount,km,trailercapasity,wheelpercent))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for("tasıyıcı_ayar"))
        else: 
            pass
            
        return render_template('addtrailer.html', trailermodel = trailermodel,user_idd=user_idd)
  
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

### 1.2.2.2 /driverdashboard/tasıyıcı_ayar/addtrailer/trailertype 
@app.route('/driverdashboard/tasıyıcı_ayar/addtrailer/trailertype/<get_trailertype>')
@login_required
def dorsemodelleri(get_trailertype):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM trailertype WHERE trailermodel_id  = %s", [get_trailertype])
    trailertype = cur.fetchall()  
    trailertypeArray = []    
    for row in trailertype:
        trailertypeObj = {
                'trailertypeid': row['trailertypeid'],
                'trailertype_name': row['trailertype_name']}
        trailertypeArray.append(trailertypeObj)
    return jsonify({'trailertype_model' : trailertypeArray})













# 2. Passenger Dashboard
@app.route("/passengerdashboard")
@login_required
def passengerdashboard():
    if session["user_type"] == 'yolcu' :
        
        return render_template("passengerdashboard.html")

    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#2.1 /passengerdashboard/newtickets kayıt olan kullanıcının dashboardunda listeleme yapmak için
@app.route("/passengerdashboard/newtickets")
@login_required
def newtickets():
    if session["user_type"] == 'yolcu' :
        
        
        cursor = mysql.connection.cursor()
        sorgu = "SELECT ticketpassengers.user_name, ticketpassengers.ticket_id, ticketpassengers.enroldate,tickets.ticketid, tickets.startdate, tickets.usertrucktrailerid, tickets.ticketsowner,tickets.firstlocation, tickets.endlocation, tickets.price,usertrucktrailer.user_trucktrailer_id, usertrucktrailer.usertruck_id, usertruck.truckbrands, usertruck.truckmodel, usertruck.truckmodeltype, usertruck.truckyear,truckbrands.markaid, truckbrands.marka_ad,truckmodel.modelid,truckmodel.model, truckmodeltype.modeltypeid,truckmodeltype.model_type_name FROM ticketpassengers, tickets,truckbrands,truckmodel, truckmodeltype,usertrucktrailer,usertruck WHERE ticketpassengers.user_name = %s AND ticketpassengers.ticket_id = tickets.ticketid AND tickets.startdate > CURRENT_DATE() AND tickets.usertrucktrailerid = usertrucktrailer.user_trucktrailer_id AND usertrucktrailer.usertruck_id = usertruck.usertruck_id AND usertruck.truckbrands = truckbrands.markaid AND usertruck.truckmodel = truckmodel.modelid AND usertruck.truckmodeltype = truckmodeltype.modeltypeid;"
        result1 = cursor.execute(sorgu,(session["username"],))


        if result1 > 0 :
            nticketdetail = cursor.fetchall()

            return render_template("newtickets.html",nticketdetail=nticketdetail)
        else:
            return render_template("newtickets.html")
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

# 2.1.1 /passengerdashboard/newtickets/deletesignedticket/{{nticketdetail.ticket_id}} yolculuğa kayıt olan kullanıcı seferini silme
# burada silinen yolculukları silinen yolculuklar tablosuna aktarılıyor tamamlandı.
@app.route("/passengerdashboard/newtickets/deletesignedticket/<path:value>")
@login_required
def deletesignedticket(value):
    if session["user_type"] == 'yolcu' :
        
        ticketid, drivername = value.split("-")
        
        cursor = mysql.connection.cursor()
        sorgu = "Select * from ticketpassengers where user_name = %s and ticket_id = %s"
        result = cursor.execute(sorgu,(session["username"],ticketid))


        if result >0 :
            cur = mysql.connection.cursor()
            sorgu2 = "INSERT INTO cancelledticketsfrpassenger(drivername,passengername,ticket_id) VALUES(%s,%s,%s)"
            cur.execute(sorgu2,(drivername,session["username"],ticketid,))

            
            deletesignedticketsorgu = "DELETE FROM ticketpassengers WHERE ticket_id = %s"
            cursor.execute(deletesignedticketsorgu,(ticketid,))
            mysql.connection.commit()
            cursor.close()
            cur.close()

            flash("Başarıyla yolculuk kaydınızı sildiniz. İptal edilen yolculuğunuz iptal ettiğim seferler tablosundan bulabilirsiniz.","success")
            return redirect(url_for("newtickets"))
        else:
            flash("Yolculuk kaydınızı silemediniz. Lütfen tekrar deneyiniz.","danger")
            return redirect(url_for("newtickets"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))





#2.2 /passengerdashboard/oldtickets
@app.route("/passengerdashboard/oldtickets")
@login_required
def oldtickets():
        if session["user_type"] == 'yolcu' :

            cursor = mysql.connection.cursor()
            sorgu = "SELECT ticketpassengers.user_name, ticketpassengers.ticket_id, ticketpassengers.enroldate,tickets.ticketid, tickets.startdate, tickets.usertrucktrailerid, tickets.ticketsowner,tickets.firstlocation, tickets.endlocation, tickets.price,usertrucktrailer.user_trucktrailer_id, usertrucktrailer.usertruck_id, usertruck.truckbrands, usertruck.truckmodel, usertruck.truckmodeltype, usertruck.truckyear,truckbrands.markaid, truckbrands.marka_ad,truckmodel.modelid,truckmodel.model,truckmodeltype.modeltypeid,truckmodeltype.model_type_name FROM ticketpassengers, tickets,truckbrands,truckmodel,truckmodeltype,usertrucktrailer,usertruck WHERE ticketpassengers.user_name = %s AND ticketpassengers.ticket_id = tickets.ticketid AND tickets.startdate < NOW() AND tickets.usertrucktrailerid = usertrucktrailer.user_trucktrailer_id AND usertrucktrailer.usertruck_id = usertruck.usertruck_id AND usertruck.truckbrands = truckbrands.markaid AND usertruck.truckmodel = truckmodel.modelid AND usertruck.truckmodeltype = truckmodeltype.modeltypeid"
            result = cursor.execute(sorgu,(session["username"],))
            if result >0 :
                old_pass_tickets = cursor.fetchall()   
                    
                return render_template("oldtickets.html",old_pass_tickets=old_pass_tickets)
            else:
                flash("Görüntülenecek sefer bulunmamaktadır","danger")
                return render_template("oldtickets.html")

        else:
            flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
            return redirect(url_for("index"))


# Yolcu tarafından veya Sürücü tarafından iptal edilen seferlerin görüntülenmesi
#2.3 /passengerdashboard/cancelledtickets
@app.route("/passengerdashboard/cancelledtickets")
@login_required
def cancelledtickets():
    if session ["user_type"] == 'yolcu' :
        cursor = mysql.connection.cursor()
        sorgu = "Select * from cancelledticketsfrpassenger where passengername = %s"
        result = cursor.execute(sorgu,(session["username"],))

        cur = mysql.connection.cursor()
        sorgu2 = "Select * from cancelledticketsfrdriver where passengername = %s"
        result2 = cur.execute(sorgu2,(session["username"],))

        if result >0 and result2 >0 :  
            cancelledticketsfrpassenger = cursor.fetchall()
            cancelledticketsfrdriver = cur.fetchall()
            return render_template("cancelledtickets.html",cancelledticketsfrpassenger=cancelledticketsfrpassenger,cancelledticketsfrdriver=cancelledticketsfrdriver)
        elif result >0 and result2 == 0:
            cancelledticketsfrpassenger = cursor.fetchall()
            return render_template("cancelledtickets.html",cancelledticketsfrpassenger=cancelledticketsfrpassenger)
        elif result == 0 and result2 >0:
            cancelledticketsfrdriver = cur.fetchall()
            return render_template("cancelledtickets.html",cancelledticketsfrdriver=cancelledticketsfrdriver)
            
        else:
            flash("Görüntülenecek iptal edilen sefer bulunmamaktadır","danger")
            return render_template("cancelledtickets.html")








# 3. Consignor Dashboard


#Taşımacılık Profil
@app.route("/consignordashboard")
def consignordashboard():
    if  session ["user_type"] == "tasıtan":
        return render_template("consignordashboard.html")
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))


# 3.1.1 Consignor Dashboard/companyprofile şirket bilgileri ekleme sayfası
@app.route("/consignordashboard/companyprofile",methods = ["GET","POST"])

@login_required
def companyprofile():
    
    
    companyformsorgu = "Select * from companyform where username = %s"
    curs = mysql.connection.cursor()
    companyformsorguresult = curs.execute(companyformsorgu,(session["username"],))
    companyinfo = curs.fetchone()
    form = CompanyForm(request.form)

    if session ["user_type"] == "tasıtan":
        if request.method == "POST" and form.validate() and companyformsorguresult == 0:
                companyname = form.companyname.data
                companydescription = form.companydescription.data
                companytypelegally = form.companytypelegally.data
                companytypefunctionally = form.companytypefunctionally.data
                companyaddress = form.companyaddress.data
                companyphone = form.companyphone.data
                companyemail = form.companyemail.data
                companywebsite = form.companywebsite.data
                companylinkedin = form.companylinkedin.data
                companyfacebook = form.companyfacebook.data
                companytwitter = form.companytwitter.data
                companyinstagram = form.companyinstagram.data
                companyyoutube = form.companyyoutube.data
                companygoogleplus = form.companygoogleplus.data
                companytaxnumber = form.companytaxnumber.data
                companytaxoffice = form.companytaxoffice.data
                companytaxadmin = form.companytaxadmin.data
                companytaxadminphone = form.companytaxadminphone.data
                companytaxadmineposta = form.companytaxadmineposta.data
                companytaxadminaddress = form.companytaxadminaddress.data
                companytaxadminidentitynumber = form.companytaxadminidentitynumber.data
                companytaxadminidentitydate = form.companytaxadminidentitydate.data
                companytaxadminidentityplace = form.companytaxadminidentityplace.data
                companycurrency = form.companycurrency.data

                cursor = mysql.connection.cursor()
                sorgu = "Insert into companyform set companyname = %s,companydescription = %s,companytypelegally = %s,companytypefunctionally = %s,companyaddress = %s,companyphone = %s,companyemail = %s,companywebsite = %s,companylinkedin = %s,companyfacebook = %s,companytwitter = %s,companyinstagram = %s,companyyoutube = %s,companygoogleplus = %s,companytaxnumber = %s,companytaxoffice = %s,companytaxadmin = %s,companytaxadminphone = %s,companytaxadmineposta = %s,companytaxadminaddress = %s,companytaxadminidentitynumber = %s,companytaxadminidentitydate = %s,companytaxadminidentityplace = %s,companycurrency = %s, username = %s"
                cursor.execute(sorgu,(companyname,companydescription,companytypelegally,companytypefunctionally,companyaddress,companyphone,companyemail,companywebsite,companylinkedin,companyfacebook,companytwitter,companyinstagram,companyyoutube,companygoogleplus,companytaxnumber,companytaxoffice,companytaxadmin,companytaxadminphone,companytaxadmineposta,companytaxadminaddress,companytaxadminidentitynumber,companytaxadminidentitydate,companytaxadminidentityplace,companycurrency,session["username"]))
                mysql.connection.commit()
                cursor.close()
                flash("Şirket bilgileriniz başarıyla güncellendi","success")
                return redirect(url_for("companyprofile"))
        elif request.method == "POST" and form.validate() and companyformsorguresult > 0:
                companyname = form.companyname.data
                companydescription = form.companydescription.data
                companytypelegally = form.companytypelegally.data
                companytypefunctionally = form.companytypefunctionally.data
                companyaddress = form.companyaddress.data
                companyphone = form.companyphone.data
                companyemail = form.companyemail.data
                companywebsite = form.companywebsite.data
                companylinkedin = form.companylinkedin.data
                companyfacebook = form.companyfacebook.data
                companytwitter = form.companytwitter.data
                companyinstagram = form.companyinstagram.data
                companyyoutube = form.companyyoutube.data
                companygoogleplus = form.companygoogleplus.data
                companytaxnumber = form.companytaxnumber.data
                companytaxoffice = form.companytaxoffice.data
                companytaxadmin = form.companytaxadmin.data
                companytaxadminphone = form.companytaxadminphone.data
                companytaxadmineposta = form.companytaxadmineposta.data
                companytaxadminaddress = form.companytaxadminaddress.data
                companytaxadminidentitynumber = form.companytaxadminidentitynumber.data
                companytaxadminidentitydate = form.companytaxadminidentitydate.data
                companytaxadminidentityplace = form.companytaxadminidentityplace.data
                companycurrency = form.companycurrency.data

                cur = mysql.connection.cursor()
                sorgu = "Update companyform set companyname = %s,companydescription = %s,companytypelegally = %s,companytypefunctionally = %s,companyaddress = %s,companyphone = %s,companyemail = %s,companywebsite = %s,companylinkedin = %s,companyfacebook = %s,companytwitter = %s,companyinstagram = %s,companyyoutube = %s,companygoogleplus = %s,companytaxnumber = %s,companytaxoffice = %s,companytaxadmin = %s,companytaxadminphone = %s,companytaxadmineposta = %s,companytaxadminaddress = %s,companytaxadminidentitynumber = %s,companytaxadminidentitydate = %s,companytaxadminidentityplace = %s,companycurrency = %s, username = %s where username = %s"
                cur.execute(sorgu,(companyname,companydescription,companytypelegally,companytypefunctionally,companyaddress,companyphone,companyemail,companywebsite,companylinkedin,companyfacebook,companytwitter,companyinstagram,companyyoutube,companygoogleplus,companytaxnumber,companytaxoffice,companytaxadmin,companytaxadminphone,companytaxadmineposta,companytaxadminaddress,companytaxadminidentitynumber,companytaxadminidentitydate,companytaxadminidentityplace,companycurrency,session["username"],session["username"]))
                mysql.connection.commit()
                cur.close()
                flash("Şirket bilgileriniz başarıyla güncellendi","success")
                return redirect(url_for("companyprofile"))
        else:
                form = CompanyForm()
                form.companyname.data =companyinfo["companyname"]
                form.companydescription.data =companyinfo["companydescription"]
                form.companytypelegally.data =companyinfo["companytypelegally"]
                form.companytypefunctionally.data =companyinfo["companytypefunctionally"]
                form.companyaddress.data =companyinfo["companyaddress"]
                form.companyphone.data =companyinfo["companyphone"]
                form.companyemail.data =companyinfo["companyemail"]
                form.companywebsite.data =companyinfo["companywebsite"]
                form.companylinkedin.data =companyinfo["companylinkedin"]
                form.companyfacebook.data =companyinfo["companyfacebook"]
                form.companytwitter.data =companyinfo["companytwitter"]
                form.companyinstagram.data =companyinfo["companyinstagram"]
                form.companyyoutube.data =companyinfo["companyyoutube"]
                form.companygoogleplus.data =companyinfo["companygoogleplus"]
                form.companytaxnumber.data =companyinfo["companytaxnumber"]
                form.companytaxoffice.data =companyinfo["companytaxoffice"]
                form.companytaxadmin.data =companyinfo["companytaxadmin"]
                form.companytaxadminphone.data =companyinfo["companytaxadminphone"]
                form.companytaxadmineposta.data =companyinfo["companytaxadmineposta"]
                form.companytaxadminaddress.data =companyinfo["companytaxadminaddress"]
                form.companytaxadminidentitynumber.data =companyinfo["companytaxadminidentitynumber"]
                form.companytaxadminidentitydate.data =companyinfo["companytaxadminidentitydate"]
                form.companytaxadminidentityplace.data =companyinfo["companytaxadminidentityplace"]
                form.companycurrency.data =companyinfo["companycurrency"]
                return render_template("companyprofile.html",form = form)
        

    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))



# 3.2 Consignordashboard/newshippingjobs ileri tarihte gerçeklecek taşıma işleri sayfası
@app.route("/consignordashboard/newshippingjobs")
@login_required
def newshippingjobs():
    if session["user_type"] == "tasıtan":
        cur = mysql.connection.cursor()
        sorgu = "Select * from shippingjobs where consignor_username = %s and shippingstartdate > CURRENT_DATE() order by shippingstartdate asc"
        result = cur.execute(sorgu,(session["username"],))

        if result > 0:
            shippingjobs = cur.fetchall()
            return render_template("newshippingjobs.html",shippingjobs = shippingjobs)
        else:
            flash("İleri tarihte gerçekleşecek taşıma işiniz bulunmamaktadır","danger")
            return render_template("newshippingjobs.html")
         
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

# 3.3 Consignordashboard/oldshippingjobs geçmiş taşıma işleri sayfası
@app.route("/consignordashboard/oldshippingjobs")
@login_required
def oldshippingjobs():
    if session["user_type"] == "tasıtan":
        cur = mysql.connection.cursor()
        sorgu = "Select * from shippingjobs where consignor_username = %s and shippingstartdate < CURRENT_DATE() order by shippingstartdate asc"
        result = cur.execute(sorgu,(session["username"],))
        if result > 0:
            shippingjobs = cur.fetchall()
            return render_template("oldshippingjobs.html",shippingjobs = shippingjobs)
        else:
            flash("Geçmiş taşıma işiniz bulunmamaktadır","danger")
            return render_template("oldshippingjobs.html")

         
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#3.3 Consignordashboard/deleteshippingjob ileri tarihte gerçeklecek taşıma işi silme sayfası


# Bu FONKSİYON SÜRÜCÜLERİN TAŞIMA İŞLERİNE KAYIT OLMAK İÇİN KULLANILACAK. FAKAT KAPASİTE KONTROLÜ YAPILACAK. YÖNEYLEM ARAŞTIRMA ALGORİTMALARI KULLANILACAK.
#3.3 drivershippingregister/<string:id>
@app.route("/drivershippingregister/<string:id>",methods =["GET","POST"])
@login_required
def drivershippingregister(id):
    if session ["user_type"] == "tasıyıcı":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from shippingjobs where jobid = %s"
        result = cursor.execute(sorgu,(id,))
        
        curs = mysql.connection.cursor()
        tıreslemesorgusu = "Select user_trucktrailer_id from usertrucktrailer where user_name = %s "
        tıreslemesorgusuresult = curs.execute(tıreslemesorgusu,(session["username"],))

        # Tırcı Öncedeb Kayıtlı mı Kontrolü
        curso = mysql.connection.cursor()
        sorgu3 = "Select * from shippingdriverregister where driverusername = %s and jobidd = %s"
        result3 = curso.execute(sorgu3,(session["username"],id,))


        if result > 0 and result3 == 0:
            shippingjobs = cursor.fetchone()
            usttiddict = curs.fetchone()
            it = iter(usttiddict.values()) 
            usertrucktrailerid = next(it)
            if request.method == "POST":
                username = session["username"]
                cur = mysql.connection.cursor()
                sorgu2 = "Insert into shippingdriverregister (jobidd,driverusername,usertrucktrailerid) VALUES (%s,%s,%s)"
                cur.execute(sorgu2,(id,username,usertrucktrailerid))
                mysql.connection.commit()
                flash("Taşıma işine başarıyla kayıt oldunuz","success")
                # Buraya yeni bir sayfa açılacak ve bu sayfada taşıma işi hakkında bilgiler olacak. Bu sayfada sürücüye ait bilgiler olacak. Sürücü bu sayfadan taşıma işini iptal edebilecek.*********************
                return redirect(url_for("index"))
            else:
                return render_template("drivershippingregister.html",shippingjobs = shippingjobs)
        else:
            flash("Böyle bir taşıma işi bulunmamaktadır veya önceden kayıt oldunuz.","danger")
            return redirect(url_for("index"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))




#3.4 Consignordashboard/enroleddrivers taşıma işine kayıtlı sürücüler sayfası
@app.route("/consignordashboard/enroleddrivers/<string:id>") 
@login_required
def enroleddrivers(id):
    if session["user_type"] == "tasıtan":
        cur = mysql.connection.cursor()
        sorgu = " Select shippingdriverregister.driverusername,shippingdriverregister.jobidd,users.username,users.email,users.user_id, usertrucktrailer.user_name, usertrucktrailer.user_trucktrailer_id , usertrucktrailer.usertruck_id, usertrucktrailer.usertrailer_id, trailermodel.trailermodelid , trailermodel.trailermodel_name, trailertype.trailertypeid, trailertype.trailertype_name, usertrailer.trailermodel_idd, usertrailer.trailertype_idd, truckbrands.marka_ad, truckbrands.markaid, truckmodel.model, truckmodel.modelid, truckmodeltype.model_type_name, truckmodeltype.modeltypeid, usertruck.truckmodel, usertruck.truckmodeltype, usertruck.truckbrands from shippingdriverregister INNER JOIN users ON shippingdriverregister.driverusername = users.username INNER JOIN usertrucktrailer ON shippingdriverregister.usertrucktrailerid = usertrucktrailer.user_trucktrailer_id INNER JOIN usertrailer ON usertrucktrailer.usertrailer_id = usertrailer.usertrailerid INNER JOIN trailermodel ON usertrailer.trailermodel_idd = trailermodel.trailermodelid INNER JOIN trailertype ON usertrailer.trailertype_idd = trailertype.trailertypeid INNER JOIN usertruck ON usertrucktrailer.usertruck_id = usertruck.usertruck_id INNER JOIN truckbrands ON usertruck.truckbrands = truckbrands.markaid INNER JOIN truckmodel ON usertruck.truckmodel = truckmodel.modelid INNER JOIN truckmodeltype ON usertruck.truckmodeltype = truckmodeltype.modeltypeid where shippingdriverregister.jobidd = %s"
        
        result = cur.execute(sorgu,(id,))
        if result > 0:
            enroleddrivers = cur.fetchall()
            return render_template("enroleddrivers.html",enroleddrivers = enroleddrivers)
        else:
            flash("Kayıtlı sürücü bulunmamaktadır veya yetkiniz yok.","warning")
            return redirect(url_for("consignordashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))


#3.5 Driverdashboard/enrolledshippingjobs taşıma işine kayıtlı sürücüler sayfası
@app.route("/driverdashboard/enrolledshippingjobs")
@login_required
def enrolledshippingjobs():
    if session["user_type"] == "tasıyıcı":
        cur = mysql.connection.cursor()
        sorgu ="Select shippingjobs.consignor_username, shippingjobs.shippingstartdate, shippingjobs.jobid, shippingjobs.shippingenddate, shippingjobs.shippingstartplace, shippingjobs.shippingendplace,users.username, users.email, shippingjobs.unitdriverfee, shippingjobs.unitdriverfeecurrency, shippingjobs.shippingcreateddate from shippingjobs INNER JOIN users ON shippingjobs.consignor_username = users.username INNER JOIN shippingdriverregister ON shippingjobs.jobid = shippingdriverregister.jobidd where shippingdriverregister.driverusername = %s"
        result = cur.execute(sorgu,(session["username"],))
        if result > 0:
            enrolledshippingjobs = cur.fetchall()
            return render_template("enrolledshippingjobs.html",enrolledshippingjobs = enrolledshippingjobs)
        else:
            flash("Böyle bir taşıma işi bulunmamaktadır veya yetkiniz yok.","danger")
            return redirect(url_for("driverdashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#3.6 Driverdashboard/enrolledshippingjobs/deleteenrolledshippingjobs/<path:id> taşıma işi sürücü tarafından iptal edilmesi
@app.route("/driverdashboard/enrolledshippingjobs/deleteenrolledshippingjobs/<string:id>")
@login_required
def deleteenrolledshippingjobs(id):
    if session["user_type"] == "tasıyıcı":
        
        cursor = mysql.connection.cursor()
        sorgu = "Select * FROM shippingdriverregister WHERE jobidd = %s and driverusername = %s"
        result = cursor.execute(sorgu,(id,session["username"],))
        curso = mysql.connection.cursor()
        sorgu2 = "Select consignor_username FROM shippingjobs WHERE jobid = %s"
        resultname = curso.execute(sorgu2,(id,))
        iddict = curso.fetchone()
        it = iter(iddict.values())    
        consignor_username = next(it)
        if result > 0:
            silsorgu = "DELETE FROM shippingdriverregister WHERE jobidd = %s and driverusername = %s"
            cursor.execute(silsorgu,(id,session["username"],))

            cur= mysql.connection.cursor()
            cancelledshippingjobsfrdriver = "INSERT INTO canc_shippingjobfr_dr (job_id,drivername,consignorname) VALUES (%s,%s,%s)"
            cur.execute(cancelledshippingjobsfrdriver,(id,session["username"],consignor_username,))
            mysql.connection.commit()
            cur.close()
            cursor.close()
            flash("Taşıma işi başarıyla iptal edildi. İptal edilen işlerinizi 'İptal Edilen Taşımacılık İşlerim Sayfasından Kontrol Edebilirsiniz' ","success")
            return redirect(url_for("driverdashboard"))
        else:
            flash("Böyle bir taşıma işi bulunmamaktadır veya yetkiniz yok.","danger")
            return redirect(url_for("driverdashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#3.6.1 /driverdashboard/enrolledshippingjobs/cancelledshippingjobs sürücü sayfasında taşıma işi iptal edilen işlerin listelenmesi
@app.route("/driverdashboard/enrolledshippingjobs/cancelledshippingjobs-driver")
@login_required
def cancelledshippingjobs():
    if session["user_type"] == "tasıyıcı":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from canc_shippingjobfr_dr where drivername = %s"
        result = cursor.execute(sorgu,(session["username"],))

        cur = mysql.connection.cursor()
        sorgu2 = "Select * from canc_shippingjobfr_consignor where drivername = %s"
        result2 = cur.execute(sorgu2,(session["username"],))
        if result > 0 and result2 > 0:
            cancelledshippingjobs_dr = cursor.fetchall()
            cancelledshippingjobs_cg = cur.fetchall()
            return render_template("cancelledshippingjobs-driver.html",cancelledshippingjobs_dr = cancelledshippingjobs_dr, cancelledshippingjobs_cg = cancelledshippingjobs_cg)
        elif result > 0 and result2 == 0:
            cancelledshippingjobs_dr = cursor.fetchall()
            return render_template("cancelledshippingjobs-driver.html",cancelledshippingjobs_dr = cancelledshippingjobs_dr)
        elif result == 0 and result2 > 0:
            cancelledshippingjobs_cg = cur.fetchall()
            return render_template("cancelledshippingjobs-driver.html",cancelledshippingjobs_cg = cancelledshippingjobs_cg)
        else:
            flash("İptal edilen taşıma işi bulunmamaktadır.","danger")
            return redirect(url_for("driverdashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

# 3.11 consignordashboard/cancelledshippingjobs-consignor tasıyıcı sayfasında taşıma işi iptal edilen işlerin listelenmesi
@app.route("/consignordashboard/cancelledshippingjobs-consignor")
@login_required
def cancelledshippingjobs_consignor():
    if session["user_type"] == "tasıtan":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from canc_shippingjobfr_consignor where consignorname = %s"
        result = cursor.execute(sorgu,(session["username"],))

        cur = mysql.connection.cursor()
        sorgu2 = "Select * from canc_shippingjobfr_dr where consignorname = %s"
        result2 = cur.execute(sorgu2,(session["username"],))
        if result > 0 and result2 > 0:
            cancelledshippingjobs_cg = cursor.fetchall()
            cancelledshippingjobs_dr = cur.fetchall()
            return render_template("cancelledshippingjobs-consignor.html",cancelledshippingjobs_cg = cancelledshippingjobs_cg, cancelledshippingjobs_dr = cancelledshippingjobs_dr)
        elif result > 0 and result2 == 0:
            cancelledshippingjobs_cg = cursor.fetchall()
            return render_template("cancelledshippingjobs-consignor.html",cancelledshippingjobs_cg = cancelledshippingjobs_cg)
        elif result == 0 and result2 > 0:
            cancelledshippingjobs_dr = cur.fetchall()
            return render_template("cancelledshippingjobs-consignor.html",cancelledshippingjobs_dr = cancelledshippingjobs_dr)
        else:
            flash("İptal edilen taşıma işi bulunmamaktadır.","danger")
            return redirect(url_for("consignordashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))









#"/ticketsdelete/<string:id>" bu sayfaya benzer bir yapı kullanılması gerekir.
#3.8 Consignordashboard/enrolledshippingjobs/deleteenrolledshippingdrivers/<string:id> taşıma işi şirket tarafından iptal edilmesi
@app.route("/consignordashboard/enrolledshippingjobs/deleteenrolledshippingdrivers/<string:id>")
@login_required
def deleteenrolledshippingdrivers(id):
    if session["user_type"] == "tasıtan":
        cursor = mysql.connection.cursor()
        #Kullanıcı ve Sefer uyumlu mu ve var mı sorgusu
        sorgu = "Select * FROM shippingjobs WHERE jobid = %s and consignor_username = %s"
        result = cursor.execute(sorgu,(id,session["username"],))
        emptydriver = "-"

        #Taşıma işine kayıtlı tırcılar var mı sorgusu
        curso = mysql.connection.cursor()
        sorgu2 = "Select * FROM shippingdriverregister WHERE jobidd = %s"
        result1 = curso.execute(sorgu2,(id,))
        if result > 0 :
            if result1 > 0:
                flash("Taşıma işine kayıtlı tırcılar olduğu için işi iptal edemezsiniz.","danger")
                return redirect(url_for("consignordashboard"))
            else:
                silsorgu = "DELETE FROM shippingjobs WHERE jobid = %s"
                cursor.execute(silsorgu,(id,))
                cur= mysql.connection.cursor()
                cancelledshippingjobsfrconsignor = "INSERT INTO canc_shippingjobfr_consignor (job_id,consignorname,drivername) VALUES (%s,%s,%s)"
                cur.execute(cancelledshippingjobsfrconsignor,(id,session["username"],emptydriver,))
                mysql.connection.commit()
                cur.close()
                cursor.close()
                flash("Taşıma işi başarıyla iptal edildi. İptal edilen işlerinizi 'İptal Edilen Taşımacılık İşlerim Sayfasından Kontrol Edebilirsiniz' ","success")
                return redirect(url_for("consignordashboard"))
        else:
            flash("Böyle bir taşıma işi bulunmamaktadır veya yetkiniz yok.","danger")
            return redirect(url_for("consignordashboard"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))

#3.9 Consignordashboard/enrolledshippingjobs/finishenrolledshippingjobs/<string:id> taşıma işi tamamlanması

#3.10 enrolleddriversdelete/<path:id> kayıtlı tırcı silme
@app.route("/enrolleddriversdelete/<path:id>")
@login_required
def enrolleddriversdelete(id):
    if session["user_type"] == "tasıtan":
        jobidd,drivername = id.split("-")
        cursor = mysql.connection.cursor()
        sorgu = "Select * FROM shippingdriverregister WHERE jobidd = %s and driverusername = %s"
        result = cursor.execute(sorgu,(jobidd,drivername,))
        if result > 0:
            silsorgu = "DELETE FROM shippingdriverregister WHERE jobidd = %s and driverusername = %s"
            cursor.execute(silsorgu,(jobidd,drivername,))
            mysql.connection.commit()
            cursor.close()
            flash("Tırcı başarıyla silindi.","danger")
            cur = mysql.connection.cursor()
            sorgu2 = "INSERT INTO canc_shippingjobfr_consignor (job_id,consignorname,drivername) VALUES (%s,%s,%s)"
            cur.execute(sorgu2,(jobidd,session["username"],drivername,))
            mysql.connection.commit()
            cur.close()
            flash("İptal edilen ve silinen sürücü bilgilerine 'İptal Edilen İşler' sayfasından ulaşabilirsiniz.","warning")

            return redirect(url_for("consignordashboard"))

                


#3.2.1 Consignordashboard/newshippingjobs/addshippingjob ileri tarihte gerçeklecek taşıma işi ekleme sayfası
@app.route("/consignordashboard/newshippingjobs/addshippingjob",methods = ["GET","POST"])
@login_required
def addshippingjob():
    if session["user_type"] == "tasıtan":
        cursor = mysql.connection.commit()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result1 = cur.execute("SELECT * FROM freightmodel")
        freightmodel = cur.fetchall()
        if result1 > 0 :
            cursor = mysql.connection.cursor()
            sorgu = ("SELECT user_id FROM users WHERE username = %s")
            result = cursor.execute(sorgu,(session["username"],))
            #MySQLdb.cursors.DictCursor'dan dolayı çektiğim veriler dicte dönüştüğü için çekmek istediğim veriyi dict içerisinde it fonksiyonuyla alıp o şekilde değişkene atayıp sonrasında database tekrar atmam gerek.
            
            iddict = cursor.fetchone()
            it = iter(iddict.values())    
            user_idd = next(it)

            if request.method == "POST":
                freightmodelid = request.form.get("freightmodel")
                freighttypeid = request.form.get("freighttype")
                shippingstartdate = request.form.get("shippingstartdate")
                shippingenddate = request.form.get("shippingenddate")
                shippingstartplace = request.form.get("shippingstartplace")
                
                shippingstartplacedetailed = request.form.get("shippingstartplacedetailed")
                shippingendplacedetailed = request.form.get("shippingendplacedetailed")

                shippingendplace = request.form.get("shippingendplace")
                
                shippingendlocationperson = request.form.get("shippingendlocationperson")
                shippingendlocationpersonphone = request.form.get("shippingendlocationphone")
                shippingendlocationpersonemail = request.form.get("shippingendlocationemail")
                
                shippingcargo = request.form.get("shippingcargo")
                shippingcargoquantity = request.form.get("shippingcargoquantity")
                shippingcargoweight = request.form.get("shippingcargoweight")
                shippingcargovolume = request.form.get("shippingcargovolume")
                
                shippingcargounitvalue = request.form.get("shippingcargounitvalue")
                shippingcargounitvaluecurrency = request.form.get("shippingcargounitvaluecurrency")

                shippingcargowidth = request.form.get("shippingcargowidth")
                shippingcargolength = request.form.get("shippingcargolength")
                shippingcargoheight = request.form.get("shippingcargoheight")

                shippingcargopackage = request.form.get("shippingcargopackage")
                shippingcargopackagequantity = request.form.get("shippingcargopackagequantity")
                shippingcargopackageweight = request.form.get("shippingcargopackageweight")
                
                shippingcargopackagewidth = request.form.get("shippingcargopackagewidth")
                shippingcargopackagelength = request.form.get("shippingcargopackagelength")
                shippingcargopackageheight = request.form.get("shippingcargopackageheight")
                
                shippingcargopackagevolume = request.form.get("shippingcargopackagevolume")
                
                shippingcargopackagetotalweight = request.form.get("shippingcargopackagetotalweight")
                shippingcargopackagetotalvolume = request.form.get("shippingcargopackagetotalvolume")
                shippingcargopackagetotalquantity = request.form.get("shippingcargopackagetotalquantity")

                shippingcargototalvaluecurrency = request.form.get("shippingcargototalvaluecurrency")
                shippingcargototalvalue = request.form.get("shippingcargototalvalue")

                shippingcargoinsurance = request.form.get("shippingcargoinsurance")
                shippingcargoinsurancevalue = request.form.get("shippingcargoinsurancevalue")
                shippingcargoinsurancecurrency = request.form.get("shippingcargoinsurancecurrency")

                shippingcargodangerousname = request.form.get("shippingcargodangerousname")
                shippingcargodangerousnumber = request.form.get("shippingcargodangerousnumber")
                shippingcargodangerousclass = request.form.get("shippingcargodangerousclass")
            
                # Birim Şoför ücreti ekle
                unitdriverfee = request.form.get("unitdriverfee")
                unitdriverfeecurrency = request.form.get("unitdriverfeecurrency")


                curs = mysql.connection.cursor()
                sql = "INSERT INTO shippingjobs (freightmodelid,freighttypeid,shippingstartdate,shippingenddate,shippingstartplace,shippingstartplacedetailed,shippingendplacedetailed,shippingendplace,shippingendlocationperson,shippingendlocationpersonphone,shippingendlocationpersonemail,shippingcargo,shippingcargoquantity,shippingcargoweight,shippingcargovolume,shippingcargounitvalue,shippingcargounitvaluecurrency,shippingcargowidth,shippingcargolength,shippingcargoheight,shippingcargopackage,shippingcargopackagequantity,shippingcargopackageweight,shippingcargopackagewidth,shippingcargopackagelength,shippingcargopackageheight,shippingcargopackagevolume,shippingcargopackagetotalweight,shippingcargopackagetotalvolume,shippingcargopackagetotalquantity,shippingcargototalvaluecurrency,shippingcargototalvalue,shippingcargoinsurance,shippingcargoinsurancevalue,shippingcargoinsurancecurrency,shippingcargodangerousname,shippingcargodangerousnumber,shippingcargodangerousclass,consignor_username,unitdriverfee,unitdriverfeecurrency) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(sql,(freightmodelid,freighttypeid,shippingstartdate,shippingenddate,shippingstartplace,shippingstartplacedetailed,shippingendplacedetailed,shippingendplace,shippingendlocationperson,shippingendlocationpersonphone,shippingendlocationpersonemail,shippingcargo,shippingcargoquantity,shippingcargoweight,shippingcargovolume,shippingcargounitvalue,shippingcargounitvaluecurrency,shippingcargowidth,shippingcargolength,shippingcargoheight,shippingcargopackage,shippingcargopackagequantity,shippingcargopackageweight,shippingcargopackagewidth,shippingcargopackagelength,shippingcargopackageheight,shippingcargopackagevolume,shippingcargopackagetotalweight,shippingcargopackagetotalvolume,shippingcargopackagetotalquantity,shippingcargototalvaluecurrency,shippingcargototalvalue,shippingcargoinsurance,shippingcargoinsurancevalue,shippingcargoinsurancecurrency,shippingcargodangerousname,shippingcargodangerousnumber,shippingcargodangerousclass,session["username"],unitdriverfee,unitdriverfeecurrency,))
                mysql.connection.commit()
                curs.close()
                
                flash("Yeni taşıma işi başarıyla eklendi","success")
                return redirect(url_for("newshippingjobs"))
            else:
                pass
            return render_template("addshippingjob.html", freightmodel = freightmodel, user_idd = user_idd)
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))



### Add Shipping Jobs Edit ### Sorun burada *************************
@app.route('/consignordashboard/editshippingjob/<string:id>', methods = ["GET","POST"])
@login_required
def editshippingjob(id):
    
    
    if request.method == "GET":
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM shippingjobs WHERE jobid = %s AND consignor_username = %s", (id,session["username"],))
        curs = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result1 = curs.execute("SELECT * FROM freightmodel")
        freightmodel = curs.fetchall()
        if result == 0:
            flash("Güncellenecek bir taşıma işi bulunamadı","danger")
            return redirect(url_for("index"))
        else:
            shippingjobs = cur.fetchone()
            cur.close()
            return render_template("editshippingjob.html", shippingjobs = shippingjobs, freightmodel = freightmodel)
    else:
        freightmodelid = request.form.get("freightmodelid")
        freighttypeid = request.form.get("freighttypeid")
        shippingstartdate = request.form.get("shippingstartdate")
        shippingenddate = request.form.get("shippingenddate")
        shippingstartplace = request.form.get("shippingstartplace")
        shippingstartplacedetailed = request.form.get("shippingstartplacedetailed")
        shippingendplacedetailed = request.form.get("shippingendplacedetailed")
        shippingendplace = request.form.get("shippingendplace")
        shippingendlocationperson = request.form.get("shippingendlocationperson")
        shippingendlocationpersonphone = request.form.get("shippingendlocationpersonphone")
        shippingendlocationpersonemail = request.form.get("shippingendlocationpersonemail")
        shippingcargo = request.form.get("shippingcargo")
        shippingcargoquantity = request.form.get("shippingcargoquantity")
        shippingcargoweight = request.form.get("shippingcargoweight")
        shippingcargovolume = request.form.get("shippingcargovolume")
        shippingcargounitvalue = request.form.get("shippingcargounitvalue")
        shippingcargounitvaluecurrency = request.form.get("shippingcargounitvaluecurrency")
        shippingcargowidth = request.form.get("shippingcargowidth")
        shippingcargolength = request.form.get("shippingcargolength")
        shippingcargoheight = request.form.get("shippingcargoheight")
        shippingcargopackage = request.form.get("shippingcargopackage")
        shippingcargopackagequantity = request.form.get("shippingcargopackagequantity")
        shippingcargopackageweight = request.form.get("shippingcargopackageweight")
        
        shippingcargopackagewidth = request.form.get("shippingcargopackagewidth")
        shippingcargopackagelength = request.form.get("shippingcargopackagelength")
        shippingcargopackageheight = request.form.get("shippingcargopackageheight")
        
        shippingcargopackagevolume = request.form.get("shippingcargopackagevolume")
        
        shippingcargopackagetotalweight = request.form.get("shippingcargopackagetotalweight")
        shippingcargopackagetotalvolume = request.form.get("shippingcargopackagetotalvolume")
        shippingcargopackagetotalquantity = request.form.get("shippingcargopackagetotalquantity")

        shippingcargototalvaluecurrency = request.form.get("shippingcargototalvaluecurrency")
        shippingcargototalvalue = request.form.get("shippingcargototalvalue")
        shippingcargoinsurance = request.form.get("shippingcargoinsurance")
        shippingcargoinsurancevalue = request.form.get("shippingcargoinsurancevalue")
        shippingcargoinsurancecurrency = request.form.get("shippingcargoinsurancecurrency")
        shippingcargodangerousname = request.form.get("shippingcargodangerousname")
        shippingcargodangerousnumber = request.form.get("shippingcargodangerousnumber")
        shippingcargodangerousclass = request.form.get("shippingcargodangerousclass")
        
        unitdriverfee = request.form.get("unitdriverfee")
        unitdriverfeecurrency = request.form.get("unitdriverfeecurrency")


    
        sql = "UPDATE shippingjobs SET freightmodelid = %s, freighttypeid = %s, shippingstartdate = %s, shippingenddate = %s, shippingstartplace = %s, shippingstartplacedetailed = %s, shippingendplacedetailed = %s, shippingendplace = %s, shippingendlocationperson = %s, shippingendlocationpersonphone = %s, shippingendlocationpersonemail = %s, shippingcargo = %s, shippingcargoquantity = %s, shippingcargoweight = %s, shippingcargovolume = %s, shippingcargounitvalue = %s, shippingcargounitvaluecurrency = %s, shippingcargowidth = %s, shippingcargolength = %s, shippingcargoheight = %s, shippingcargopackage = %s, shippingcargopackagequantity = %s, shippingcargopackageweight = %s, shippingcargopackagewidth = %s, shippingcargopackagelength = %s, shippingcargopackageheight = %s, shippingcargopackagevolume = %s, shippingcargopackagetotalweight = %s, shippingcargopackagetotalvolume = %s, shippingcargopackagetotalquantity = %s, shippingcargototalvaluecurrency = %s, shippingcargototalvalue = %s, shippingcargoinsurance = %s, shippingcargoinsurancevalue = %s, shippingcargoinsurancecurrency = %s, shippingcargodangerousname = %s, shippingcargodangerousnumber = %s, shippingcargodangerousclass = %s, unitdriverfee = %s, unitdriverfeecurrency = %s WHERE jobid = %s"
        cursor = mysql.connection.cursor() 
        cursor.execute(sql,(freightmodelid, freighttypeid, shippingstartdate, shippingenddate, shippingstartplace, shippingstartplacedetailed, shippingendplacedetailed, shippingendplace, shippingendlocationperson, shippingendlocationpersonphone ,  shippingendlocationpersonemail ,  shippingcargo ,  shippingcargoquantity ,  shippingcargoweight ,  shippingcargovolume ,  shippingcargounitvalue ,  shippingcargounitvaluecurrency ,  shippingcargowidth ,  shippingcargolength ,  shippingcargoheight ,  shippingcargopackage ,  shippingcargopackagequantity ,  shippingcargopackageweight ,  shippingcargopackagewidth ,  shippingcargopackagelength ,  shippingcargopackageheight ,  shippingcargopackagevolume ,  shippingcargopackagetotalweight ,  shippingcargopackagetotalvolume ,  shippingcargopackagetotalquantity ,  shippingcargototalvaluecurrency ,  shippingcargototalvalue ,  shippingcargoinsurance ,  shippingcargoinsurancevalue ,  shippingcargoinsurancecurrency ,  shippingcargodangerousname ,  shippingcargodangerousnumber ,  shippingcargodangerousclass ,  unitdriverfee ,  id,unitdriverfeecurrency,))
        mysql.connection.commit()
        cursor.close()
        flash("Taşıma işi başarıyla güncellendi","success")
        return redirect(url_for("shippingjobs"))

## *************** Edit Shipping Jobs Freighttype Burası Çalışmıyor Düzenle ******************* ##
@app.route('/consignordashboard/editshippingjob/<string:id>/freighttype/<get_freighttype>')
def get_yük_sınıfları_jobs_edit(get_freighttype):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM freighttype WHERE freightmodel_idd  = %s", [get_freighttype])
    freighttype = cur.fetchall()  
    freighttypeArray = []
    for row in freighttype:
        freighttypeObj = {
            "freighttypeid": row["freighttypeid"],
            "freighttype_name": row["freighttype_name"]
        }
        freighttypeArray.append(freighttypeObj)
    return jsonify({'freighttype_freightmodel' : freighttypeArray})






### Shipping Jobs '/shippingjobs' ana sekmesinde tüm işleri tırcıya göre listeleme ayarlanması lazım###
@app.route('/shippingjobs')
def shippingjobs():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM shippingjobs WHERE shippingstartdate >= CURRENT_DATE()")
    
    if result > 0:
        shippingjobs = cur.fetchall()
        return render_template("shippingjobs.html", shippingjobs = shippingjobs)
    else:
        flash("Henüz hiç taşıma işi eklenmemiş","danger")
        return render_template("shippingjobs.html")


### Shipping Jobs Arama Butonları Kullanılarak ###
@app.route('/shippingjobss', methods = ["GET","POST"])
def shippingjobss():
    if request.method == "POST":
        search = request.form.get("search")
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM shippingjobs WHERE shippingstartdate >= CURRENT_DATE() AND shippingstartplace LIKE %s OR shippingendplace LIKE %s OR shippingstartdate LIKE %s OR shippingenddate LIKE %s OR shippingcargodangerousclass LIKE %s", ["%"+search+"%","%"+search+"%","%"+search+"%","%"+search+"%","%"+search+"%"])
        if result > 0:
            #HTMlden gelen verileri alıp %s ile sql sorgusuna gönderiyoruz
            
            
            shippingjobs = cur.fetchall()
            flash("Aranan kriterlere uygun taşıma işi bulundu","success")
            return render_template("shippingjobs.html", shippingjobs = shippingjobs)
        else:
            flash("Aranan kriterlere uygun taşıma işi bulunamadı","danger")
            return redirect(url_for("shippingjobs"))
    else:
        flash("Arama yapmak için gerekli alanları doldurunuz","danger")
        return redirect(url_for("shippingjobs"))
        

### 1.2.2.2 /driverdashboard/tasıyıcı_ayar/addtrailer/yük_sınıfları ### <get_yük_sınıfları> vscode bu şekilde kabul etmiyor hata veriyor. get_yük_sınıfları bu şeilde de kod parçası çalışmaz. ###
@app.route('/consignordashboard/newshippingjobs/addshippingjob/freighttype/<get_freighttype>')
def get_yük_sınıfları(get_freighttype):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM freighttype WHERE freightmodel_idd  = %s", [get_freighttype])
    freighttype = cur.fetchall()  
    freighttypeArray = []
    for row in freighttype:
        freighttypeObj = {
            "freighttypeid": row["freighttypeid"],
            "freighttype_name": row["freighttype_name"]
        }
        freighttypeArray.append(freighttypeObj)
    return jsonify({'freighttype_freightmodel' : freighttypeArray})


# 3.4 Consignordashboard/oldshippingjobs geçmiş tarihli taşıma işleri sayfası

# 3.5 Consignordashboard/cancelledshippingjobs iptal edilen taşıma işleri sayfası





#Register Kayıt Olma   Get-Post Request      ##########
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        identitynumber = form.identitynumber.data
        address = form.address.data
        user_type = form.user_type.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,email,username,password,identitynumber,address,user_type) VALUES(%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password,identitynumber,address,user_type))
  
# Veritabanından bilgi çekerken commit yapmaya gerek yok fakat değişiklik yaptığımız için yukarda(ekleme) commit kullanacağız.
        mysql.connection.commit()      
        cursor.close()
        flash("Başarıyla Kayıt Oldunuz...","success")
       
        return redirect(url_for("login"))
    else:

        return render_template("register.html",form = form)



##Login

@app.route("/login", methods= ["GET","POST"] )
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
       username = form.username.data 
       password_entered = form.password.data

       cursor = mysql.connection.cursor()

       sorgu = "Select * from users where username = %s"

       result = cursor.execute(sorgu,(username,))

       if result > 0:
            #DataBaseden veri alma fonksiyonu
            data = cursor.fetchone()
            #Database'e aktarılan şifre şifrelendği içi sha256 fonksiyonunu kullanacağız
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                
                
                
                #Session Oturum Kontrolü Sadece giriş yapınca çıkış yap gözükücek bu session kontrolü if else ile navbar html sayfasına da aktardık

                session["logged_in"] = True
                session["username"] = username   
                
                #Session UserType'ı almamız lazım navbar ve dashboardları daha da geliştirmek için
                cursor = mysql.connection.cursor()
                sorgu = "Select * from users where username = %s"
                result = cursor.execute(sorgu,(session["username"],))
                if result > 0:
                    data = cursor.fetchone()
                    user_type = data["user_type"]
                    session["user_type"] = user_type
                    flash("Başarıyla Session Alındı .","success")
                    return redirect(url_for("index"))
                else:
                    flash("Session Alınmadı .","success")
                    return redirect(url_for("index"))

            else:
                flash("Parolanızı veya Kullanıcı Adınızı Yanlış Girdiniz.","danger")
                return redirect(url_for("login"))
       else: 
            flash("Parolanızı veya Kullanıcı Adınızı Yanlış Girdiniz.","danger")

            return redirect(url_for("login"))



    return render_template("login.html", form = form)


# LogOut İşlemi
@app.route("/logout")
def logout():
    session.clear()
    flash("Başarıyla Çıkış Yapıldı.","success")
    return redirect(url_for("index"))

# Yolculuk Seferi Oluşturma !!! oluşturulacak yolculuk seferlerinde kullanıcı geçmiş tarihi seçememesi lazım.
@app.route("/addtickets",methods = ["GET","POST"])
@login_required
def addtickets():
    if session["user_type"] == 'tasıyıcı' :   
        curs = mysql.connection.cursor()
        tıreslemesorgusu = "Select user_trucktrailer_id from usertrucktrailer where user_name = %s "
        result = curs.execute(tıreslemesorgusu,(session["username"],))
        
        if result > 0 :
            #Çekilern veri sözlük olarak geldi bunun için iter yaptık.
            usttiddict = curs.fetchone()
            it = iter(usttiddict.values())    
            usertrucktrailerid = next(it)
            form = TicketsForm(request.form)
            if request.method == "POST" and form.validate():
                firstlocation = form.firstlocation.data
                endlocation = form.endlocation.data
                routeaddress = form.routeaddress.data
                startdate = form.startdate.data
                price = form.price.data
                capacity = form.capacity.data
                cursor = mysql.connection.cursor()
                sorgu = "Insert into tickets(usertrucktrailerid,ticketsowner,firstlocation,endlocation,routeaddress,startdate,price,capacity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sorgu,(usertrucktrailerid,session["username"],firstlocation,endlocation,routeaddress,startdate,price,capacity))
                mysql.connection.commit()
                cursor.close()
                flash("Yolculuk Seferiniz Başarıyla Eklendi","success")
                return redirect(url_for("driverdashboard"))
            return render_template("addtickets.html",form = form)
        else :
            flash("Yolcu seferi ekleyebilmek için Tır-Dorse ilişkisi eklemelisiniz.","danger")
            return redirect(url_for("tasıyıcı_ayar"))
    else :
        flash("Bu sayfayı görüntülemek için yetkiniz yok","danger")
        return redirect(url_for("index"))



#Yolculuk Formu
class TicketsForm(Form):
    firstlocation = StringField("Başlangıç Şehri Giriniz",validators=[validators.Length(min = 3, max = 30)])
    endlocation = StringField("Bitiş Şehri Giriniz",validators=[validators.Length(min = 3, max = 30)])
    routeaddress = TextAreaField("Ayrıntılı Rota Adresinizi Giriniz",validators=[validators.Length(min = 10)])
    startdate = DateField("Başlangıç Tarihini Giriniz")

    price = StringField("Taşımacılık Ücretinizi Giriniz")
    capacity = IntegerField("Taşıyabileciğiniz Yolcu Sayısını Giriniz")





#Yolculuk Seferleri Sayfası (/tickets) !!!! Yolculuk seferlerini tarihi düzgün alıp web sayfasından alınan Post Request isteğindeki seçilen tarihe eşit olan tarihdeki seferleri databaseden getirme işlemini ekle
# TARİH DÜZELTMESİ AYARLANDI....
@app.route("/tickets")
def tickets():
    cursor = mysql.connection.cursor()

    sorgu = "SELECT * FROM tickets WHERE startdate > CURRENT_DATE() AND (capacity - (SELECT COUNT(*) FROM ticketpassengers WHERE ticket_id = tickets.ticketid)) > 0"
    result = cursor.execute(sorgu)
                                    #FETCHONE 1 tane veriyi almak için kullanılan fonksiyon FETCHALL tümünü almak için kullanılan fonksiyon
    if result > 0:
        tickets = cursor.fetchall()
        
        return render_template("tickets.html",tickets = tickets)
    else:
        return render_template("tickets.html")

#### Yolculuk Seferine Yolcuların Kayıt Olması ("passengersignup")
@app.route("/passengersignup/<string:id>",methods =["GET","POST"])
@login_required
def passengersignup(id):
    if session["user_type"] == 'yolcu' :  
        cursor = mysql.connection.cursor()
        sorgu = "Select * from tickets where ticketid = %s"
        result = cursor.execute(sorgu,(id,))

        curs = mysql.connection.cursor()
        capasitysorgu = "Select capacity from tickets where ticketid = %s"
        result2 = curs.execute(capasitysorgu,(id,))
        capasitydict = curs.fetchone()
        it = iter(capasitydict.values())    
        sumcapasity = next(it)
        if result > 0 :
            trip = cursor.fetchone()
            if request.method == "POST" :
                cur = mysql.connection.cursor()
                sorgu = "INSERT INTO ticketpassengers (user_name,ticket_id) VALUES(%s,%s)"
                cur.execute(sorgu,(session["username"],id))
    
                mysql.connection.commit()
                cur.close()



                flash("Yolculuğa başarıyla kayıt oldunuz. Güncel Seferlerim sekmesinde görebilirsiniz.","success")
                return redirect(url_for("passengerdashboard"))
            return render_template("passengersignup.html",trip=trip,sumcapasity=sumcapasity)
        else:
            flash("Bu sayfaya geçmek için kayıt olun.","danger")
            return render_template("index.html")
    else:
        flash("Yolculuğa yalnızca başlangıçta yolcu olarak kayıt olan kullanıcılar kayıt olabilir. Lütfen yeniden kayıt olun.","danger")
        return redirect(url_for("register"))





# ***** Passengerticketsdetail html ve direverticketdetail html sayfası tamamlandığında bu kısımları silmek gerekiyor. *****
#Yolculuk Detay Sayfası session["username"] üzerinden çalışıyor bunu ilerde session userid ye çevirmek gerekiyor.
@app.route("/driverdashboard/ticketdetail/<string:id>")
@login_required
def ticketdetail(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from tickets where ticketid = %s and ticketsowner = %s"
    result = cursor.execute(sorgu,(id,session["username"]))

    if result > 0 :
        ticket = cursor.fetchone()
        return render_template("ticketdetail.html",ticket = ticket)
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok.","danger")
        return render_template("index.html")




#Yolculuk Detay Sayfası session["username"] üzerinden çalışıyor bunu ilerde session userid ye çevirmek gerekiyor.
# Yolculuk Detay Sayfası Yolcu için de aynı şekilde çalışıyor bunu ayrı ayrı yapmak gerekiyor. enroledpassengers ve passengerticketdetail.
@app.route("/driverdashboard/enroledpassengers/<string:id>")
@login_required
def enroledpassengers(id):
    if session["user_type"] == 'tasıyıcı' :
        #if request.method == "GET": 
            cursor = mysql.connection.cursor()
            sorgu = "SELECT ticketpassengers.user_name, ticketpassengers.ticket_id, ticketpassengers.enroldate, tickets.ticketid, tickets.startdate, tickets.usertrucktrailerid, tickets.ticketsowner,tickets.firstlocation, tickets.endlocation, tickets.price ,users.username, users.email, users.name  FROM ticketpassengers, tickets, users WHERE ticketpassengers.ticket_id = %s AND ticketpassengers.ticket_id = tickets.ticketid AND ticketpassengers.user_name = users.username ;"
            result = cursor.execute(sorgu,(id,))
    #FETCHONE 1 tane veriyi almak için kullanılan fonksiyon FETCHALL tümünü almak için kullanılan fonksiyon ayrıca burda 
    # ticketlara kayıt olan yolcuları da getirmek gerekiyor.
    
    # ********* Sorgu güncellendi enroledpassengers.html sayfasını oluştur verileri al ve göster.

            
            tickets = cursor.fetchall()
            return render_template("enroledpassengers.html",tickets = tickets)
        
            
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok.","danger")
        return render_template("index.html")

# Sürücünün Oluşturduğu Yolculuklara Kayıt Olan Yolcuları Silme ve İptal Edilen Yolculukları Kayıt Ediyor(Path kullanımı <string:id> tek değişkeni htmlden almak için <path:id> birden çok değişkeni almak için kullandık gönderdiğimiz değişkenler arasına benzersiz imleç koyup o imlece göre fonk içinde ayırarak değişkenlere atadık split fonksiyonu).
@app.route("/driverdashboard/enroledpassengers/enroledpassdelete/<path:id>")
@login_required
def enroledpassdelete(id):
    if session["user_type"] == 'tasıyıcı' :

        ticketid, passusname = id.split("-")        
        
        cursor = mysql.connection.cursor()
        sorgu = "Select * from ticketpassengers where user_name = %s and ticket_id = %s "
        result = cursor.execute(sorgu,(passusname,ticketid))
        if result > 0:
            silsorgu = "Delete from ticketpassengers where user_name = %s and ticket_id = %s"
            cursor.execute(silsorgu,(passusname,ticketid))
            
            cur = mysql.connection.cursor()
            canceledticket = "INSERT INTO cancelledticketsfrdriver (ticket_id,drivername,passengername) VALUES (%s,%s,%s)"
            cur.execute(canceledticket,(ticketid,session["username"],passusname))
            
            mysql.connection.commit()
            cursor.close()

            flash(" Seferinize Kayıtlı Yolcuyu Başarıyla Sildiniz Silinen Yolculuklarınıza ve Yolcularınıza Silinen Yolculuk ve Yolcular sekmesinden bakabilirsiniz.","warning")
            return redirect(url_for("driverdashboard"))
        else:
            flash("Böyle bir sefer veya seferinize kayıtlı böyle bir kullanıcı yok.","danger")
            return render_template("index.html")




# Yolculuk Seferi Silme
#Önemli nokta başka kullanıcıların oluşturduğu sefer silinmemeli ve giriş yapmadan girilmemeli session kontrol 
# ******** Sefere Kayıt Olmuş Yolcu Olması Durumunda Silme işlemi farklı olması gerekecek....... ***** Yapıldı
@app.route("/ticketsdelete/<string:id>")
@login_required
def delete(id):
    if session["user_type"] == 'tasıyıcı' :


        cursor = mysql.connection.cursor()
        #Kullanıcı ve Sefer uyumlu mu ve var mı sorgusu
        varsorgu = "Select * from tickets where ticketsowner = %s and ticketid = %s "

        result = cursor.execute(varsorgu,(session["username"],id))

        kaydolansorgu = "Select * from ticketpassengers where ticket_id = %s"
        kaydolanresult = cursor.execute(kaydolansorgu,(id,))

        if result > 0:
            if kaydolanresult > 0:    
                flash("Bu seferde kayıtlı yolcu olduğu için seferi silemezsiniz. Yolculuk sefer ayarlarından silmek istediğiniz yolculuktaki kayıtlı yolcuları siliniz.","danger")
                return redirect(url_for("ticketssettings"))
            else:
                silsorgu = "Delete from tickets where ticketid = %s"

                cursor.execute(silsorgu,(id,))

                mysql.connection.commit()
                flash("Yolculuk Seferiniz Başarıyla Silindi","success") 
                return redirect(url_for("driverdashboard"))
        else:
            flash("Böyle bir sefer yok veya bu işleme yetkiniz yok","danger")
            return redirect(url_for("index"))
    else:
        flash("Bu sayfayı görüntülemek için yetkiniz yok.","danger")
        return render_template("index.html")

#Yolculuk Seferi Güncelleme
@app.route("/ticketsedit/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()

        sorgu = "Select * from tickets where ticketid = %s and ticketsowner =%s"
        result = cursor.execute(sorgu,(id,session["username"]))

        if result == 0 :
            flash("Güncellenecek sefer bulunmamaktadır.","warning")
            return redirect(url_for("index"))
        
        else:
            ticket = cursor.fetchone()
            form = TicketsForm()
            
            form.firstlocation.data = ticket["firstlocation"]
            form.endlocation.data = ticket["endlocation"]
            form.routeaddress.data = ticket["routeaddress"]
            form.startdate.data = ticket["startdate"]
            form.price.data = ticket["price"]
            form.capacity.data = ticket["capacity"]
            return render_template("update.html",form = form)


            
    else:
        #POST REQUEST KISIM
        form = TicketsForm(request.form)

        newFirstlocation = form.firstlocation.data
        newEndlocation = form.endlocation.data
        newRouteaddress = form.routeaddress.data
        newStartdate = form.startdate.data
        newPrice = form.price.data
        newCapacity = form.capacity.data

        sorgu2 ="Update tickets Set firstlocation = %s, endlocation = %s,routeaddress = %s,startdate = %s,price = %s,capacity = %s where ticketid = %s"

        cursor = mysql.connection.cursor()
        cursor.execute(sorgu2,(newFirstlocation,newEndlocation,newRouteaddress,newStartdate,newPrice,newCapacity,id))
       
        mysql.connection.commit()

        flash("Başarıyla Seferiniz Güncellendi","success")
        return redirect(url_for("driverdashboard"))
       
# Yolculuk Arama URL
@app.route("/ticketsearch",methods = ["GET","POST"] )
def ticketsearch ():
    if request.method == "GET":
        flash("Bu şekilde arama yapamazsınız.","danger")
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()

        sorgu = "Select * from tickets where firstlocation like '%" + keyword + "%' "

        result = cursor.execute(sorgu)

        if result == 0 :
            flash("Aranan Konumda yolculuk bulunamadı.","warning")
            return redirect(url_for("tickets"))

        else:
            tickets = cursor.fetchall()
            return render_template("tickets.html",tickets = tickets)

# Yolculuk Arama Gerçekçi
@app.route("/ticketsearchy",methods = ["GET","POST"])
def ticketsearchy ():
    if request.method == "GET":
        flash("Bu şekilde arama yapamazsınız.","danger")
        return redirect(url_for("index"))
    else:
        flocation = request.form.get("flocation")
        elocation = request.form.get("elocation")
        sdate = request.form.get("sdate")
        cursor = mysql.connection.cursor()

        sorgu = "Select * from tickets where firstlocation like '%" + flocation + "%' and endlocation like '%" + elocation + "%' and startdate like '%" + sdate + "%' "

        result = cursor.execute(sorgu)

        if result == 0 :
            flash("Aradığınız kriterlere uygun sefer bulunmamaktadır.","warning")
            return redirect(url_for("tickets"))
        else:
            tickets = cursor.fetchall()
            return render_template("tickets.html",tickets = tickets)
            

# Mapbox API Deneme
@app.route("/mapboxexample")
def mapbox():
    return render_template("mapboxexample.html")




























if __name__ == "__main__":
    app.run(debug=True)