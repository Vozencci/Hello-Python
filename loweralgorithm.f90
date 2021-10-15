program loweralgorithm
	implicit none
	
	real,dimension(:,:),allocatable::A
	real,dimension(:),allocatable::b,x
	integer::n,i,j
	
	print*,"Dimension de n:"
	read*,n
	
	allocate(A(n,n),b(n),x(n))
	
	do i=1,n
		do j=1,i
			print*,"A(",i,",",j,")=?"
			read*,A(i,j)
		end do
	end do
	
	do i=1,n
		print*,"b(",i,")=?"
		read*,b(i)
	end do
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	do i=1,n
		if (i==1) then
			x(i)=b(i)/A(i,i)
		else
			do j=1,i-1
					x(i)=(b(i)-A(i,j)*x(j))/A(i,i)
			end do
		end if
		print*,"x(",i,")=",x(i)
	end do
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	deallocate(A)
	deallocate(b)
	deallocate(x)
	
end program loweralgorithm
