from flask import Flask,render_template,request,send_file
import os
from PIL import Image


app=Flask(__name__)


@app.route("/",methods=["POST","GET"])
def home():
	if request.method=="POST":
		file1=request.files.getlist('files[]')
		f=[]
		for i in file1:
			f.append(i.filename)
			i.save(f'static/{i.filename}')
		imagelist=[]
		for j in f:
			new=Image.open(f"static/{j}")
			im1=new.convert('RGB')
			imagelist.append(im1)
		im1.save(f'static/myImages.pdf',save_all=True, append_images=imagelist)
		for i in file1:
			os.remove(f'static/{i.filename}')
		return render_template('pdf_download.html',value='static/myImages.pdf')
	return render_template("upload_img.html")




@app.route('/download')
def download_file():
	return send_file(pdf_path, as_attachment=True)




if __name__=="__main__":
	app.run(debug=True)

'''
		file1.save(f'static/images/{file1.filename}')
		img_path = f'static/images/{file1.filename}'
		pdf_path = f'static/images/'
		for i in file1.filename:
			if i==".":
				pdf_path+="-"
			else:
				pdf_path+=i
		pdf_path+=".pdf"
		image = Image.open(img_path) 
		pdf_bytes = img2pdf.convert(image.filename) 
		file = open(pdf_path, "wb") 
		file.write(pdf_bytes) 
		image.close() 
		file.close()
		os.remove(f'static/images/{file1.filename}')
		return render_template('pdf_download.html',value=pdf_path)'''