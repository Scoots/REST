namespace RESTWebService
{
  using System;
  using System.ServiceModel;

  [ServiceContract]
  public interface IRESTWebService
  {
    /// <summary>
    /// Creates a new user
    /// </summary>
    /// <param name="first">The first name to insert into the database.</param>
    /// <param name="last">The last name to insert into the database.</param>
    /// <param name="nickname">The nickname to insert into the database.</param>
    /// <returns>The JSON string for Python</returns>
    [OperationContract]
    string CreateUser(string first, string last, string nickname);

    /// <summary>
    /// Modifies an existing user
    /// </summary>
    /// <param name="userId">The user id to modify</param>
    /// <param name="field">The field we wish to modify</param>
    /// <param name="value">The new value of the selected field</param>
    /// <returns>The JSON string for Python</returns>
    [OperationContract]
    string ModifyUser(int userId, string field, string value);

    /// <summary>
    /// Creates a BattleLog with the specified information
    /// </summary>
    /// <param name="attacker">The attacker's id</param>
    /// <param name="defender">The defender's id</param>
    /// <param name="winner">The winner's id</param>
    /// <param name="start">The start time</param>
    /// <param name="end">The end time</param>
    /// <returns>The JSON string for Python</returns>
    [OperationContract]
    string CreateBattleLog(int attacker, int defender, int winner, DateTime start, DateTime end);

    //[OperationContract]
    //CompositeType GetDataUsingDataContract(CompositeType composite);

    //// TODO: Add your service operations here
  }


  // Use a data contract as illustrated in the sample below to add composite types to service operations.
  //[DataContract]
  //public class CompositeType
  //{
  //  bool boolValue = true;
  //  string stringValue = "Hello ";

  //  [DataMember]
  //  public bool BoolValue
  //  {
  //    get { return boolValue; }
  //    set { boolValue = value; }
  //  }

  //  [DataMember]
  //  public string StringValue
  //  {
  //    get { return stringValue; }
  //    set { stringValue = value; }
  //  }
  //}
}
