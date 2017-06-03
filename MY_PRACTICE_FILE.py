import scipy
import scipy.ndimage
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image

a = scipy.ndimage.imread("dhoni.jpg")
#print np.shape(a)
a_np = np.array(a)
#print a_np
color_img = np.dstack((a_np[:,:,0], a_np[:,:,1], a_np[:,:,2]))
color_img_pr = Image.fromarray(color_img)
color_img_pr.show()
gray_img = a_np[:,:,0]
#print gray_img
#print np.shape(gray_img)
raw_img = Image.fromarray(gray_img)
raw_img.show()
cov_mat = gray_img - 0.75*np.mean(gray_img, axis = 1)
eig_val, eig_vec = np.linalg.eig(np.cov(cov_mat))
p = np.size(eig_vec, axis =1)
idx = np.argsort(eig_val)
idx = idx[::-1]
eig_vec = eig_vec[:,idx]
eig_val = eig_val[idx]
#print eig_val
#print eig_val.shape
numpc = 100
if numpc <p or numpc >0:
	eig_vec = eig_vec[:, range(numpc)]

score = np.dot(eig_vec.T, cov_mat)
recon = np.dot(eig_vec, score) + 0.33*np.mean(gray_img, axis = 1).T

#print recon
recon_img_mat = np.uint8(np.absolute(recon))

recon_img = Image.fromarray(recon_img_mat)
recon_img.show()
#print np.shape(recon_img)


#..................................................................

r_img = a_np[:,:,1]
#print gray_img
#print np.shape(gray_img)
raw_img_r = Image.fromarray(r_img)
raw_img_r.show()
cov_mat_r = r_img - 0.75*np.mean(r_img, axis = 1)
eig_val_r, eig_vec_r = np.linalg.eig(np.cov(cov_mat_r))
p = np.size(eig_vec_r, axis =1)
idx_r = np.argsort(eig_val_r)
idx = idx[::-1]
eig_vec_r = eig_vec_r[:,idx]
eig_val_r = eig_val_r[idx]

eig_vec_r = eig_vec[:, range(numpc)]

score_r = np.dot(eig_vec_r.T, cov_mat_r)
recon_r = np.dot(eig_vec_r, score_r) + 0.33*np.mean(r_img, axis = 1).T

#print recon
recon_img_mat_r = np.uint8(np.absolute(recon_r))

recon_img_mat_r = Image.fromarray(recon_img_mat_r)
recon_img_mat_r.show()

# ...............................................................


b_img = a_np[:,:,2]
#print gray_img
#print np.shape(gray_img)
raw_img_b = Image.fromarray(r_img)
raw_img_b.show()
cov_mat_b = b_img - 0.75*np.mean(b_img, axis = 1)
eig_val_b, eig_vec_b = np.linalg.eig(np.cov(cov_mat_b))
p = np.size(eig_vec_b, axis =1)
idx_b = np.argsort(eig_val_r)
idx = idx[::-1]
eig_vec_b = eig_vec_b[:,idx]
eig_val_b = eig_val_b[idx]
#print eig_val
#print eig_val.shape
#numpc = 50
#if numpc <p or numpc >0:
eig_vec_b = eig_vec_b[:, range(numpc)]

score_b = np.dot(eig_vec_b.T, cov_mat_b)
recon_b = np.dot(eig_vec_b, score_b) + 0.33*np.mean(b_img, axis = 1).T

#print recon
recon_img_mat_b = np.uint8(np.absolute(recon_b))

recon_img_mat_b = Image.fromarray(recon_img_mat_b)
recon_img_mat_b.show()

# ..................................................

recon_color_img = np.dstack((recon_img_mat, recon_img_mat_r, recon_img_mat_b))
recon_color_img = Image.fromarray(recon_color_img)
recon_color_img.show()
recon_color_img.label("hi")











