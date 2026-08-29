import { BrowserRouter, Route, Routes } from "react-router"
import SigninPage from "./pages/SigninPage"
import SignUpPage from "./pages/SignUpPage"
import ChatAppPage from "./pages/ChatAppPage"
import { Toaster } from "sonner"


function App() {
  return <>
  <Toaster richColors/>
  <BrowserRouter>
    <Routes>
      {/* public routes (Khong phai xac minh danh tinh) */}
      <Route
       path="/signin"
       element={<SigninPage/>}
      />
            <Route
       path="/signup"
       element={<SignUpPage/>}
      />



      {/* protectecr routes (duong dan phai dang nhap)*/}
      {/* todo: tao protected routes */}
            <Route
       path="/"
       element={<ChatAppPage/>}
      />

    </Routes>
  
  </BrowserRouter>
  
  </>
}

export default App
