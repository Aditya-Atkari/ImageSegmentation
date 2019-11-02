import matplotlib.pyplot as plt
import cv2
import imageio as im
import random
arr=im.imread('tom.bmp')
R=arr[:,:,0]
G=arr[:,:,1]
B=arr[:,:,2]

#print(R)
#print(G)
#print(B)

print(str(arr.shape))

'''
plt.subplot(1,3,1)
plt.imshow(R)
plt.subplot(1,3,2)
plt.imshow(G)
plt.subplot(1,3,3)
plt.imshow(B)
plt.show()
'''
ran=1
cost=[0 for i in range(ran)]
cluster_set=[]
c_pixels_set=[]
for w in range(ran):
	c=[]
	for i in range(0,5):
		c.append([random.randint(0,arr.shape[0]-1),random.randint(0,arr.shape[1]-1)])
	print(c)

	#c_pixels=[[arr(c[i][0],c[i][1],0), arr(c[i][0],c[i][1],1), arr(c[i][0],c[i][1],2)] for i in range(len(c)) ]
	c_pixels=[]
	for i in range(len(c)):
		c_pixels.append([arr[c[i][0],c[i][1],0], arr[c[i][0],c[i][1],1], arr[c[i][0],c[i][1],2]] )


	cluster=[[] for i in range(len(c))]

	def choose_cluster(arr,c_p):
		
		for x in range(0,arr.shape[0]):
			for y in range(0,arr.shape[1]):
				d=9999;
				i_main=-1
				for i in c_pixels:
					dist= ( (i[0]-arr[x,y,0])**2 + (i[1]-arr[x,y,1])**2 + (i[2]-arr[x,y,2])**2)**(0.5)
					#dist=((arr[x,y,0]-arr[i[0],i[1],0])**2+(arr[x,y,1]-arr[i[0],i[1],1])**2+(arr[x,y,2]-arr[i[0],i[1],2])**2)**(1/2)
					if(dist<d):
						d=dist
						i_main=c_pixels.index(i)
				cluster[i_main].append([x,y])
				cost[w]+=d
		return cluster




	def new_cluster_centers(c_pixels,arr,cluster):
		flag=1
		while(flag==1):
			new_cluster=choose_cluster(arr,c_pixels)
			if(cluster == new_cluster):
				flag=0
			else:
				
				for i in cluster:
					r_avg=0
					g_avg=0
					b_avg=0
					for j in i:
						r_avg+=arr[j[0],j[1],0]
						

						g_avg+=arr[j[0],j[1],1]
						
					
						b_avg+=arr[j[0],j[1],2]
					
					r_avg=r_avg/len(i)
					g_avg=r_avg/len(i)
					b_avg=r_avg/len(i)

					c_pixels[i][0]=r_avg
					c_pixels[i][1]=g_avg
					c_pixels[i][2]=b_avg
		return(cluster,c_pixels)

	retrn=new_cluster_centers(c_pixels,arr,cluster)
	cluster_set.append(retrn[0])
	c_pixels_set.append(retrn[1])


def new_img(cluster,c_pixels):
	for i in cluster:
		for j in i:
			arr[j[0],j[1],0]=c_pixels[cluster.index(i)][0]
			arr[j[0],j[1],1]=c_pixels[cluster.index(i)][1]
			arr[j[0],j[1],2]=c_pixels[cluster.index(i)][2]



	#plt.show()



plt.subplot(1,2,1)
plt.imshow(arr)

w=cost.index(min(cost))
new_img(cluster_set[w],c_pixels_set[w])
	#print(cluster)



plt.subplot(1,2,2)
plt.imshow(arr)
plt.show()