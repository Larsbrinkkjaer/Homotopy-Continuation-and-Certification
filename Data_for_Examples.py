import sympy as sp

#Example 1:
x1=sp.symbols('x1') #Variables of the system including t.
F_1=4-x1**4 #Polynomial system we want to solve
#Polynomial systems including variables with specified parameters:
Polynomial_System_1a=F_1 #Random gamma
Polynomial_System_1b=(F_1,100,-1) #gamma=-1, 100 iterations.
Polynomial_System_1c=(F_1,100,1j) #gamma=i, 100 iterations.

#Example 2:
x1=sp.symbols('x1') #Variables of the system including t.
F_2=x1**4-4 #Polynomial system we want to solve
Polynomial_System_2a=(F_2,10e-12,0,10,1) #gamma=1, 10 iterations, tolerance in newton iteration 10^{-12}, 0 newton iterations
Polynomial_System_2b=(F_2,10e-12,1,10,1) #gamma=1, 10 iterations, tolerance in newton iteration 10^{-12}, 1 newton iterations
Polynomial_System_2c=(F_2,10e-12,3,10,1) #gamma=1, 10 iterations, tolerance in newton iteration 10^{-12}, 3 newton iterations

#Example 3:
x1=sp.symbols('x1') #Variables of the system including t.
F_3=x1**4-4 #Polynomial system we want to solve
Polynomial_System_3=(F_3,10,1) #gamma=1, 10 iterations, tolerance in newton iteration 10^{-12}, 0 newton iterations

#Example 4:
x1,x2=sp.symbols('x1 x2') #Variables of the system including t.
F_4a=x1**2-1000*x1,x2-1 #Polynomial system we want to solve
F_4b=x2**2+x1+1,x1+x2+3 #Polynomial system we want to solve
Polynomial_System_4a=(F_4a,100,1) #gamma=1, 100 iterations
Polynomial_System_4b=(F_4b,100,1) #gamma=1, 100 iterations

#Example 5:
x1,x2=sp.symbols('x1 x2') #Variables of the system including t.
F_5=x1**2+x2**2-1,(x1-1)**2+(x2-1)**2-1 #Polynomial system we want to solve
Polynomial_System_5a=(F_5,100,(1+1j)/(2**(1/2)),1e+17) #gamma=(1+i)/sqrt(2), 100 iterations, max_chance=10^{18}
Polynomial_System_5b=(F_5,100,(1+1j)/(2**(1/2)),1e+19) #gamma=(1+i)/sqrt(2), 100 iterations, max_chance=10^{19}

#Example 6:
x1=sp.symbols('x1') #Variables of the system including t.
F_6a=x1-2 #Polynomial system we want to solve
G_6a=x1**2-1 #Specific start system, which is not total degree.
degrees_6a=[2] #Degrees of start system
F_6b=x1**2-1000*x1 #Polynomial system we want to solve
G_6b=x1**2-1 #Specific start system, which is happens to be total degree.
degrees_6b=[2] #Degrees of start system
projective_transformation_6=(0.8+0.6j,0.2+0.4j)
Polynomial_System_6a=(F_6a,G_6a,degrees_6a,10000,0.8+0.6j) #gamma=0.8+0.6i, 10000 iterations, specified start system.
Polynomial_System_6b=(F_6b,G_6b,degrees_6b,10000,0.8+0.6j) #gamma=0.8+0.6i, 10000 iterations, specified start system
Polynomial_System_6a_proj=(F_6a,G_6a,degrees_6a,projective_transformation_6,10000)
Polynomial_System_6b_proj=(F_6b,G_6b,degrees_6b,projective_transformation_6,10000)

#Example 7:
x1,x2,x3=sp.symbols('x1 x2 x3')
F_7=x1**2-1,x2**2-2*x1,x3**2-x2*x1
Polynomial_System_7=F_7

#Example 9: (2 link planar robot):
c1,s1,c2,s2=sp.symbols('c1 s1 c2 s2')
link_lengths_2R=[2,1]
ball_position_start=[1.02319452,1.12513782] #Tip of second link should be positioned here
ball_position_end=[2,0] #Tip of second link should be positioned at (2,0)
F_planar_robot=link_lengths_2R[0]*c1+link_lengths_2R[1]*(c1*c2-s1*s2)-ball_position_start[0],link_lengths_2R[0]*s1+link_lengths_2R[1]*(c1*s2+s1*c2)-ball_position_start[1],c1**2+s1**2-1,c2**2+s2**2-1
F_planar_robot_new=link_lengths_2R[0]*c1+link_lengths_2R[1]*(c1*c2-s1*s2)-ball_position_end[0],link_lengths_2R[0]*s1+link_lengths_2R[1]*(c1*s2+s1*c2)-ball_position_end[1],c1**2+s1**2-1,c2**2+s2**2-1
U_comp_planar_robot=c1*c2-s1*s2-c1,c1*s2+s1*c2-c2
Polynomial_System_2R=(F_planar_robot,1000,(1+1j)/(2**(1/2))) #We specify gamma to ensure consistent solutions even though it should work for any random gamma.

#Example 10 (6R-serial link robot):
x21,x22,x23,x31,x32,x33,x41,x42,x43,x51,x52,x53=sp.symbols('x21 x22 x23 x31 x32 x33 x41 x42 x43 x51 x52 x53')
cos_angles=[0,0,2**(0.5)/2,0,0] #Cosine and sine of twist angles between joints
sin_angles=[1,1,2**(0.5)/2,1,1]
link_lengths=[3,2,1,1,1] #Length of links
offsets=[8,8,8,8] #Length of offsets
x1_tuple=[0.6,0.8,0] #Iniital direction of the first link
x6_tuple=[0,0.6,0.8] #Final direction of the ball
ball_position=[9.62065271,11.23851923,10.97423149] #Position of ball
ball_position_new=[10,10,10] #New position of ball
F_6R_serial=x21*x21+x22*x22+x23*x23-1,x31*x31+x32*x32+x33*x33-1,x41*x41+x42*x42+x43*x43-1,x51*x51+x52*x52+x53*x53-1,x1_tuple[0]*x21+x1_tuple[1]*x22+x1_tuple[2]*x23-cos_angles[0],x31*x21+x32*x22+x33*x23-cos_angles[1],x31*x41+x32*x42+x33*x43-cos_angles[2],x51*x41+x52*x42+x53*x43-cos_angles[3],x51*x6_tuple[0]+x52*x6_tuple[1]+x53*x6_tuple[2]-cos_angles[4],(link_lengths[0]/sin_angles[0])*(x1_tuple[1]*x23-x1_tuple[2]*x22)+(link_lengths[1]/sin_angles[1])*(x22*x33-x23*x32)+(link_lengths[2]/sin_angles[2])*(x32*x43-x33*x42)+(link_lengths[3]/sin_angles[3])*(x42*x53-x43*x52)+(link_lengths[4]/sin_angles[4])*(x52*x6_tuple[2]-x53*x6_tuple[1])+offsets[0]*x21+offsets[1]*x31+offsets[2]*x41+offsets[3]*x51-ball_position[0],(link_lengths[0]/sin_angles[0])*(-x1_tuple[0]*x23+x1_tuple[2]*x21)+(link_lengths[1]/sin_angles[1])*(-x21*x33+x23*x31)+(link_lengths[2]/sin_angles[2])*(-x31*x43+x33*x41)+(link_lengths[3]/sin_angles[3])*(-x41*x53+x43*x51)+(link_lengths[4]/sin_angles[4])*(-x51*x6_tuple[2]+x53*x6_tuple[0])+offsets[0]*x22+offsets[1]*x32+offsets[2]*x42+offsets[3]*x52-ball_position[1],(link_lengths[0]/sin_angles[0])*(x1_tuple[0]*x22-x1_tuple[1]*x21)+(link_lengths[1]/sin_angles[1])*(x21*x32-x22*x31)+(link_lengths[2]/sin_angles[2])*(x31*x42-x32*x41)+(link_lengths[3]/sin_angles[3])*(x41*x52-x42*x51)+(link_lengths[4]/sin_angles[4])*(x51*x6_tuple[1]-x52*x6_tuple[0])+offsets[0]*x23+offsets[1]*x33+offsets[2]*x43+offsets[3]*x53-ball_position[2] #Polynomial system for the given parameters.
F_6R_serial_new=F_6R_serial=x21*x21+x22*x22+x23*x23-1,x31*x31+x32*x32+x33*x33-1,x41*x41+x42*x42+x43*x43-1,x51*x51+x52*x52+x53*x53-1,x1_tuple[0]*x21+x1_tuple[1]*x22+x1_tuple[2]*x23-cos_angles[0],x31*x21+x32*x22+x33*x23-cos_angles[1],x31*x41+x32*x42+x33*x43-cos_angles[2],x51*x41+x52*x42+x53*x43-cos_angles[3],x51*x6_tuple[0]+x52*x6_tuple[1]+x53*x6_tuple[2]-cos_angles[4],link_lengths[0]*(x1_tuple[1]*x23-x1_tuple[2]*x22)+link_lengths[1]*(x22*x33-x23*x32)+link_lengths[2]*(x32*x43-x33*x42)+link_lengths[3]*(x42*x53-x43*x52)+link_lengths[4]*(x52*x6_tuple[2]-x53*x6_tuple[1])+offsets[0]*x21+offsets[1]*x31+offsets[2]*x41+offsets[3]*x51-ball_position_new[0],link_lengths[0]*(-x1_tuple[0]*x23+x1_tuple[2]*x21)+link_lengths[1]*(-x21*x33+x23*x31)+link_lengths[2]*(-x31*x43+x33*x41)+link_lengths[3]*(-x41*x53+x43*x51)+link_lengths[4]*(-x51*x6_tuple[2]+x53*x6_tuple[0])+offsets[0]*x22+offsets[1]*x32+offsets[2]*x42+offsets[3]*x52-ball_position_new[1],link_lengths[0]*(x1_tuple[0]*x22-x1_tuple[1]*x21)+link_lengths[1]*(x21*x32-x22*x31)+link_lengths[2]*(x31*x42-x32*x41)+link_lengths[3]*(x41*x52-x42*x51)+link_lengths[4]*(x51*x6_tuple[1]-x52*x6_tuple[0])+offsets[0]*x23+offsets[1]*x33+offsets[2]*x43+offsets[3]*x53-ball_position_new[2] #New polynomial system