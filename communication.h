#pragma once

#include <string>

class Communication
{
public:
    Communication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : mConnectionName(rConnectionName), mIsConnectionMaster(IsConnectionMaster) { }

    virtual ~Communication() { }

    virtual void Connect() = 0;
    virtual void Disconnect() = 0;
    virtual void Send(const std::size_t SendSize, const std::size_t SendDataId) = 0;
    virtual void Receive(const std::size_t SendSize, const std::size_t SendDataId) = 0;

protected:
    std::string GetConnectionName() const {return mConnectionName;}
    int GetEchoLevel() const              {return mEchoLevel;}
    bool GetIsConnectionMaster() const    {return mIsConnectionMaster;}
    bool GetPrintTiming() const           {return mPrintTiming;}
    bool GetIsConnected() const           {return mIsConnected;}

private:
    std::string mConnectionName;
    int mEchoLevel = 1;
    bool mIsConnectionMaster = false;
    bool mPrintTiming = false;
    bool mIsConnected = false;
};