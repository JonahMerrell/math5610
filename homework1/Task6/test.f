     
      program main
      real sval
      real*8 dval
      integer ipows, ipowd
      call smaceps(sval,ipows)
      call dmaceps(dval,ipowd)
      print *, sval, dval
      print *, ipows, ipowd
      stop
      end
      
      
      