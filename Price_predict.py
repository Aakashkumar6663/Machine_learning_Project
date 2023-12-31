import math
import streamlit as st
import pickle
import pandas as pd

bike_name=['TVS Star City Plus', 'TVS Apache RTR 180cc', 'Yamaha FZ S V',
       'Yamaha FZs 150cc', 'Honda CB Hornet 160R',
       'Hero Splendor Plus Self', 'Royal Enfield Classic Desert',
       'Yamaha YZF-R15 2.0 150cc', 'Bajaj Pulsar NS200',
       'Bajaj Discover 100M', 'Bajaj Discover 125M',
       'Bajaj Pulsar NS200 ABS', 'Suzuki Gixxer SF 150cc',
       'Hero Splendor iSmart Plus', 'Yamaha FZ V 2.0',
       'Hero Super Splendor 125cc', 'Honda CBF Stunner 125cc',
       'Bajaj Pulsar 150cc', 'Honda X-Blade 160CC ABS',
       'Bajaj Avenger 220cc', 'Honda CB Unicorn 150cc', 'KTM Duke 200cc',
       'Honda CBR 150R 150cc', 'Royal Enfield Thunderbird 350cc',
       'Royal Enfield Bullet Electra', 'Royal Enfield Classic 350cc',
       'Mahindra Centuro NXT 110cc', 'Hero Hunk 150cc', 'Yamaha FZ 150cc',
       'Royal Enfield Bullet 350cc', 'TVS Apache RTR 160cc',
       'Honda CB Shine 125cc', 'Honda Dream Yuga 110cc',
       'Yamaha SZ 150cc', 'Suzuki Gixxer 150cc',
       'Bajaj Avenger Cruise 220', 'Bajaj Pulsar 220cc',
       'Hero CD Deluxe 100cc', 'Bajaj Platina 125cc',
       'Hero Karizma ZMR 223cc', 'Bajaj Pulsar 180cc',
       'Bajaj CT 100 100cc', 'Bajaj Pulsar 135LS', 'Bajaj Pulsar 220F',
       'Yamaha FZ16 150cc', 'Bajaj V15 150cc', 'Hero Splendor plus 100cc',
       'Bajaj Pulsar RS200', 'Suzuki Gixxer 150cc SP',
       'Yamaha YZF-R15 S 150cc', 'TVS Apache RTR 160',
       'Honda CB ShineSP 125cc', 'Honda CBR 250R',
       'Hero Passion Pro 100cc', 'Hero Splendor Plus 100cc',
       'Royal Enfield Electra 350cc', 'TVS Phoenix Disc 125cc',
       'Bajaj Discover 150cc', 'Bajaj Avenger Street 220',
       'Bajaj Pulsar NS 200', 'Honda X-Blade 160cc',
       'Bajaj Discover 125ST', 'Hero Splendor Plus Kick',
       'Hero Karizma 223cc', 'Hero Splendor 100cc', 'Yamaha Fazer 150cc',
       'Yamaha Gladiator 125cc', 'Hero Karizma R 223cc',
       'TVS Apache RTR 200', 'Hero HF Deluxe i3s', 'Suzuki Gixxer SF Fi',
       'Hero Splendor iSmart 110cc', 'Bajaj Platina 100cc',
       'TVS Star City 110cc', 'Bajaj Platina  Alloy', 'TVS Sport 100cc',
       'Bajaj Pulsar AS200', 'Yamaha SZ-RR 150cc',
       'Bajaj Discover 150F Disc', 'Yamaha Saluto 125cc Disc',
       'Honda CBR 250R ABS', 'Bajaj V12 125cc', 'Bajaj V12 125cc Disc',
       'Yamaha Fazer 25 250cc', 'Hero Xpulse 200T',
       'Hero Passion Xpro 110cc', 'Royal Enfield Classic 500cc',
       'Hero HF Deluxe 100cc', 'Honda CB Twister 110cc',
       'Bajaj Pulsar 125cc Disc', 'Honda Dream Neo 110cc',
       'Bajaj Pulsar AS150', 'Hero Achiever 150cc', 'TVS Apache 150cc',
       'Hero HF Deluxe Self', 'Royal Enfield Standard 350cc',
       'Bajaj Pulsar NS160', 'Suzuki Intruder 150cc', 'Bajaj CT 100 B',
       'Hero Passion Pro 110cc', 'Yamaha YZF-R15 150cc',
       'Hero Ignitor Disc 125cc', 'Bajaj Avenger Street 150',
       'Hero Glamour Disc 125cc', 'Hero HF Dawn 100cc',
       'Suzuki Slingshot Plus 125cc', 'Mahindra Centuro Rockstar 110cc',
       'Mahindra Centuro 110cc', 'Bajaj Pulsar RS200 ABS',
       'Hero Splendor Plus IBS', 'Bajaj Discover 135cc',
       'Bajaj Discover 125cc', 'Honda Livo 110cc', 'Honda CB Unicorn 160',
       'Bajaj Boxer BM150', 'Hero Glamour 125cc', 'Bajaj Discover 100cc',
       'Bajaj Avenger Street 180', 'Honda CB Trigger 150cc',
       'Bajaj Platina 100cc ComforTec', 'Honda CB Unicorn Dazzler',
       'Hero Xtreme 200R', 'Bajaj V15 150cc POWER', 'Yamaha SZR 150cc',
       'TVS Star Sport 100cc', 'Hero CD Dawn 100cc', 'Hero Passion 100cc',
       'Suzuki Intruder SP 150cc', 'Hero Passion Plus 100cc',
       'Hero CBZ 150cc', 'Yamaha FZS FI 150cc', 'Suzuki GS 150 R',
       'Yamaha FZ25 250cc', 'Hero CBZ Xtreme 150cc', 'Yamaha SZ RR V',
       'Hero Honda Splendor 100cc', 'Hero Ignitor 125cc',
       'Bajaj Pulsar 200cc', 'Royal Enfield Bullet Twinspark',
       'Bajaj Pulsar 150cc Rear', 'Hero Splendor NXG 100cc',
       'Royal Enfield Thunderbird 500cc', 'Hero Achiever Disc 150cc',
       'Bajaj Pulsar 200 NS', 'Hero Passion Pro i3S', 'Hero Xtreme 150cc',
       'Bajaj Boxer CT100', 'Hero Splendor Pro 100cc',
       'Suzuki Hayate 110cc', 'Yamaha Fazer FI V',
       'Royal Enfield Classic 350cc-Redditch', 'TVS Victor 110cc Disc',
       'Honda Livo Disc 110cc', 'Bajaj Discover 110cc', 'Hero CD 100SS',
       'Hero Honda Splendor Plus', 'Bajaj Discover 100T',
       'Hero HF Deluxe self', 'Royal Enfield Bullet 350cc',
       'Bajaj Discover 125cc Disc', 'TVS Flame 125cc',
       'Royal Enfield Machismo 350cc', 'TVS Victor 110cc',
       'Rajdoot GTX 175cc', 'KTM RC 200cc', 'Bajaj Pulsar  180cc',
       'Honda CD 110 Dream', 'Hero Xtreme Sports Rear', 'Bajaj CT 100 ES',
       'Bajaj  Pulsar 180cc', 'Bajaj Discover 150F', 'Bajaj CT 100 Alloy',
       'Hero Xtreme 200R ABS', 'Honda CBR 150R Deluxe',
       'Hero Glamour i3s 125cc', 'Honda SP125 Disc BS6',
       'Bajaj Platina 110 H', 'KTM Duke 390cc', 'Hero Splendor Plus 100',
       'Yamaha RX135 135cc 4-Speed', 'Hero Splendor iSmart 100cc',
       'Royal Enfield Bullet 350', 'Suzuki Gixxer 150cc Dual',
       'Royal Enfield Machismo 500cc', 'Bajaj Platina 110 CBS',
       'Hero Xtreme Sports 150cc', 'Suzuki Intruder 150cc FI',
       'Hero Xtreme Sports 149cc', 'Hero HF Deluxe Eco', 'Bajaj XCD 125',
       'Bajaj CT110 ES Alloy', 'Bajaj Avenger Street 160',
       'Hero Splendor+ 100cc', 'Royal Enfield Classic Chrome',
       'Suzuki Heat 125cc', 'Bajaj Pulsar NS160 Rear',
       'Bajaj Discover150 150cc', 'Bajaj Discover 125T',
       'Bajaj Pulsar 150cc Classic', 'Yamaha Saluto 125cc',
       'Hero Passion XPRO 110', 'TVS Fiero 150cc', 'Yamaha Fazer25 250cc',
       'Bajaj Platina Alloy ES', 'TVS Jive 110cc', 'Bajaj Boxer AT100',
       'Bajaj Discover 150S Disc', 'TVS Radeon 110cc Drum',
       'Suzuki Gixxer 150cc ABS', 'Suzuki Hayate EP 110cc',
       'Yamaha SZX 150cc', 'Hero CBZ Star 160cc', 'Hero Passion PRO ',
       'Bajaj Avenger 200cc', 'Hero Honda Ambition 135cc',
       'Royal Enfield Standard 500cc', 'Bajaj Pulsar 135LS 135cc',
       'Bajaj CT 100 KS', 'Honda CB Unicorn 150', 'Hero Glamour PGM Fi',
       'LML Freedom DX 110cc', 'Yezdi Classic 250cc', 'TVS Star 100cc',
       'Bajaj XCD 135', 'Bajaj Avenger 150cc', 'Hero HF Deluxe 100',
       'Yamaha Fazer FI 150cc', 'Yamaha SS 125 125cc',
       'TVS Victor GX 110cc', 'Hero Passion Pro TR', 'TVS Sports plus ES',
       'Hero Glamour Fi 125cc', 'Bajaj Pulsar NS 200cc',
       'Yamaha YBR 110cc', 'Bajaj CT 100 Spoke', 'Yamaha Crux 110cc',
       'Yamaha Saluto RX 110cc', 'TVS Phoenix 125cc',
       'Hero Splendor Pro Classic', 'Yamaha FZ Fi Version',
       'Yamaha SZS 150cc', 'Suzuki Zeus 125cc',
       'Yamaha Saluto 125cc-Special Edition', 'Bajaj Avenger 180cc',
       'Bajaj Pulsar 150cc Neon', 'Hero CBZ Xtreme 150',
       'TVS Apache RR310', 'Yamaha RX-Z 135cc', 'Yamaha Libero G5 110cc',
       'Bajaj Discover150S 150cc', 'Hero i Smart 125cc',
       'Hero Splendor Plus ', 'Hero Karizma 223 cc', 'TVS MAX 4R 110cc',
       'Mahindra Pantero 110cc', 'Hero Ambition 135cc',
       'Hero Hunk Rear Disc']

city=['Ahmedabad', 'Bangalore', 'Delhi', 'Mumbai', 'Faridabad', 'Mettur',
       'Hyderabad', 'Kaithal', 'Gurgaon', 'Noida', 'Nashik', 'Allahabad',
       'Nadiad', 'Lucknow', 'Jaipur', 'Karnal', 'Gorakhpur', 'Vidisha',
       'Hosur', 'Agra', 'Vadodara', 'Jalandhar', 'Surat', 'Chennai',
       'Pune', 'Visakhapatnam', 'Thrissur', 'Ernakulam', 'Barasat',
       'Kolkata', 'Bhubaneshwar', 'Bagalkot', 'Bhopal', 'Arrah',
       'Patiala', 'Ranga Reddy', 'Mandi', 'Ludhiana', 'Siliguri',
       'Aurangabad', 'Meerut', 'Rewari', 'Ahmednagar', 'Wardha',
       'Chandigarh', 'Thane', 'Jabalpur', 'Rohtak', 'Rajkot', 'Varanasi',
       'Kanpur', '24 Pargana', 'Kota', 'Banka', 'Banki', 'Pali',
       'Chhatarpur', 'Katihar', 'Rudrapur', 'Mysore', 'Bikaner', 'Malout',
       'Unnao', 'Godhara', 'Ghaziabad', 'Ranchi', 'Satara', 'Siwan',
       'Bhiwani', 'Nizamabad', 'Ujjain', 'Coimbatore', 'Palakkad',
       'Tiruvallur', 'Panchkula', 'Nanjangud', 'Jhansi', 'Sonipat',
       'Puttur', 'Hoshiarpur', 'Gohana', 'Gautam Buddha Nagar',
       'Durgapur', 'Palwal', 'Chatrapur', 'Howrah', 'Panipat',
       'Bharatpur', 'Vellore', 'Ambala', 'Rajahmundry', 'Belgaum',
       'Balaghat', 'Jatani', 'Asansol', 'Bilaspur', 'Thanjavur',
       'Raigarh(mh)', 'Mandi Dabwali', 'Basti', 'Bolpur', 'Aligarh',
       'Ratnagiri', 'Muktsar', 'Thiruvananthapuram', 'Indore', 'Chaksu',
       'Bharuch', 'Patna', 'Simdega', 'Pathankot', 'Kharar', 'Jhalawar',
       'Saharanpur', 'Solapur', 'Gwalior', 'Jammu', 'Katni', 'Khedbrahma',
       'Valsad', 'Hooghly', 'Gurdaspur', 'Mohali', 'Amritsar', 'Dadri',
       'Durg', 'Lansdowne', 'Jaisalmer', 'Kolhapur', 'Dungarpur',
       'Sri Ganganagar', 'Kottayam', 'Navi Mumbai', 'Chinsurah',
       'Bhatinda', 'Khalilabad', 'Dehradun', 'Anand', 'Sambalpur',
       'Purnia', 'Kalyan', 'Jodhpur', 'Sheikhpura', 'Guwahati',
       'Pondicherry', 'Sirsa', 'Raipur', 'Navsari', 'Ramanagar',
       'Udaipur', 'Vijayawada', 'Nalagarh', 'Nagpur', 'Una', 'Gandhidham',
       'Chakan', 'Shivpuri', 'Arkalgud', 'Rupnagar', 'Kanchipuram',
       'Medak', 'Ganaur', 'Amraoti', 'Mangalore', 'Deolali', 'Jhajjar',
       'Jagdalpur', 'Ankleshwar', 'Ranoli', 'Cuttack', 'Raiwala',
       'Guntur', 'Badarpur', 'Adalaj', 'Alipore', 'Bhawani Mandi',
       'Mughalsarai', 'Thiruvallur', 'Udaipurwati', 'Rasra', 'Latur',
       'Krishna', 'Gangaikondan', 'Madurai', 'Uluberia', 'Ajmer',
       'Poonamallee', 'Hissar', 'Kanyakumari', 'Bihar Shariff',
       'Goa-panaji', 'Dhanbad', 'Kolar', 'Bahadurpur', 'Budhlada',
       'Haldwani', 'Gandhinagar', 'Muzaffarnagar', 'Adyar', 'Raigarh',
       'Kasba', 'Anjar', 'Badaun', 'Dakshina Kannada', 'Alwar',
       'Surendranagar', 'Alibag', 'Sonepat', 'Burdwan', 'Mohammadabad',
       'Sangareddy', 'Shimla', 'Azamgarh', 'Chenani', 'Kanpur Nagar',
       'Trivandrum', 'Kurukshetra', 'Dhariawad', 'Chikamaglur', 'Jalaun',
       'Parola', 'Bareilly', 'Salem', 'Indi', 'Muzaffarpur', 'Bardhaman',
       'Jalgaon', 'Panvel', 'Ambikapur', 'Junagadh', 'Faridkot',
       'Karim Nagar', 'Manali', 'Gadwal', 'Mathura', 'Khandwa', 'Sitapur',
       'Anantapur', 'Pinjore', 'Qadian', 'Sangrur', 'Jorhat', 'Palanpur',
       'Narnaul', 'Palamu', 'Falakata', 'Porbandar', 'Dwarka', 'Rangpo',
       'Cannanore (kannur)', 'Baghpat', 'Moradabad', 'Naihati',
       'Darbhanga', 'Nawanshahr', 'Yamuna Nagar', 'Vasai', 'Roorkee',
       'Aluva', 'Sirsi', 'Silchar', 'Bhiwadi', 'Baripara', 'Namakkal',
       'Aquem', 'Bellary', 'Virar', 'Udhampur', 'Dhamtari', 'Vandalur',
       'Motihari', 'Dharwar', 'Jhunjhunu', 'Bijnor', 'Tirunelveli',
       'Yemmiganur', 'Bokaro', 'Mehsana', 'Puri', 'Hamirpur(hp)',
       'Rajouri', 'Begusarai', 'Goregaon', 'Bally', 'Kachchh', 'Nagaur',
       'Bahadurgarh', 'Mansa', 'Amravati', 'Tiruchirappalli', 'Nanded',
       'Chhindwara', 'Jamnagar', 'Zirakpur', 'Barabanki', 'Margao',
       'Nabha', 'Perumbavoor', 'Nazira', 'Samastipur', 'Nellore',
       'Pratapgarh', 'Thangadh', 'Chitradurga', 'Virudhunagar', 'Karwar',
       'Ganganagar', 'Deesa', 'Gadchiroli', 'Gangaghat', 'Secunderabad',
       'Bhuj', 'Vastral', 'Phagwara', 'Kheda', 'Swaimadhopur', 'Jobner',
       'Gondia', 'Bulandshahr', 'Bundi', 'Hamirpur', 'Bidar', 'Ghazipur',
       'Tumkur', 'Sanand', 'Kartarpur', 'Bhavnagar', 'Ranip', 'Suri',
       'Batala', 'Chinchwad', 'Dhubri', 'Deoria', 'Solan', 'Akot',
       'Alappuzha', 'Bhiwandi', 'Shillong', 'Sholapur', 'Osmanabad',
       'Kendua', 'Uran', 'Jaunpur', 'Hisar', 'Satna', 'Bhilai Nagar',
       'Baloda', 'Anantnag', 'Silvasa', 'Hospet', 'Palai', 'Sundargarh',
       'Sidhi']

owner=['First Owner', 'Second Owner', 'Third Owner',
       'Fourth Owner Or More']

brand=['TVS', 'Yamaha', 'Honda', 'Hero', 'Royal Enfield', 'Bajaj',
       'Suzuki', 'KTM', 'Mahindra', 'Rajdoot', 'LML', 'Yezdi']

pipe=pickle.load(open('bike_pipe_.pkl','rb'))
st.title("Bike Price Prediction")


col1=st.selectbox('Select Bike ',sorted(bike_name))
col2=st.selectbox('Select Your City',sorted(city))

kms_driven= st.number_input('Kilometers Driven')

col3=st.selectbox('Select Owner Type',sorted(owner))

age=st.number_input('Bike Age')

power=st.number_input('Power (CC)')
col4=st.selectbox('Select Bike Brand',sorted(brand))

if st.button('Predict Price'):
       bike=col1
       city=col2
       kms_driven=kms_driven
       owner=col3
       bike_age=age
       power_=power
       brand=col4
       df=pd.DataFrame([[bike,city,kms_driven,owner,bike_age,power_,brand]])


       result=pipe.predict(pd.DataFrame([[bike,city,kms_driven,owner,bike_age,
                                          power_,brand]],
                                        columns=['bike_name','city','kms_driven','owner','bike_age',
                                                 'power (cc)','brand']))

       result_1='Rs'+' '+str(math.ceil(result))
       st.header(result_1)
