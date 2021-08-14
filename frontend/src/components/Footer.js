import React from 'react'

const Footer = () => {
    return (
        <footer className="flex-shrink- on-top">
        <div className="bg-gray-800">
          <div className="max-w-screen-xl mx-auto py-10 px-4 sm:px-6 md:flex md:items-center md:justify-between text-gray-400">
            <div className="flex justify-center md:order-2 space-x-2">
              <div className="inline-block pl-6">
                <a href="mailto:xiepin225@gmail.com" target="_blank" rel="noreferrer noopener" className="hover:text-gray-300 transition duration-150 ease-in-out">
                  <span className="sr-only">Email</span>
                  <svg stroke="currentColor" fill="currentColor" strokeWidth={0} viewBox="0 0 20 20" className="w-6 h-6 fill-current" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                  </svg>
                </a>
              </div>
              <div className="inline-block pl-6">
                <a href="https://www.linkedin.com" target="_blank" rel="noreferrer noopener" className="hover:text-gray-300 transition duration-150 ease-in-out">
                  <span className="sr-only">LinkedIn</span>
                  <svg stroke="currentColor" fill="currentColor" strokeWidth={0} viewBox="0 0 448 512" className="w-6 h-6 fill-current" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z" />
                  </svg>
                </a>
              </div>
              <div className="inline-block pl-6">
                <a href="https://discord.com" target="_blank" rel="noreferrer noopener" className="hover:text-gray-300 transition duration-150 ease-in-out">
                  <span className="sr-only">Discord</span>
                  <svg stroke="currentColor" fill="currentColor" strokeWidth={0} viewBox="0 0 448 512" className="w-6 h-6 fill-current" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M297.216 243.2c0 15.616-11.52 28.416-26.112 28.416-14.336 0-26.112-12.8-26.112-28.416s11.52-28.416 26.112-28.416c14.592 0 26.112 12.8 26.112 28.416zm-119.552-28.416c-14.592 0-26.112 12.8-26.112 28.416s11.776 28.416 26.112 28.416c14.592 0 26.112-12.8 26.112-28.416.256-15.616-11.52-28.416-26.112-28.416zM448 52.736V512c-64.494-56.994-43.868-38.128-118.784-107.776l13.568 47.36H52.48C23.552 451.584 0 428.032 0 398.848V52.736C0 23.552 23.552 0 52.48 0h343.04C424.448 0 448 23.552 448 52.736zm-72.96 242.688c0-82.432-36.864-149.248-36.864-149.248-36.864-27.648-71.936-26.88-71.936-26.88l-3.584 4.096c43.52 13.312 63.744 32.512 63.744 32.512-60.811-33.329-132.244-33.335-191.232-7.424-9.472 4.352-15.104 7.424-15.104 7.424s21.248-20.224 67.328-33.536l-2.56-3.072s-35.072-.768-71.936 26.88c0 0-36.864 66.816-36.864 149.248 0 0 21.504 37.12 78.08 38.912 0 0 9.472-11.52 17.152-21.248-32.512-9.728-44.8-30.208-44.8-30.208 3.766 2.636 9.976 6.053 10.496 6.4 43.21 24.198 104.588 32.126 159.744 8.96 8.96-3.328 18.944-8.192 29.44-15.104 0 0-12.8 20.992-46.336 30.464 7.68 9.728 16.896 20.736 16.896 20.736 56.576-1.792 78.336-38.912 78.336-38.912z" />
                  </svg>
                </a>
              </div>
            </div>
            <div className="mt-8 md:mt-0 md:order-1">
              <p className="text-center text-base leading-6">
                © {/* */}2021{/* */} {/* */}Stephen Xie{/* */}. All rights reserved.
              </p>
            </div>
          </div>
        </div>
      </footer>
    )
}

export default Footer
