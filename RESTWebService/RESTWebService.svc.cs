namespace RESTWebService
{
  using System;

  // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "RESTWebService" in code, svc and config file together.
  public class RESTWebService : IRESTWebService
  {
    /// <summary>
    /// Reference to our database for the service to use
    /// </summary>
    private readonly REST db = new REST();

    /// <summary>
    /// Creates a new user
    /// </summary>
    /// <param name="first">The first name to insert into the database.</param>
    /// <param name="last">The last name to insert into the database.</param>
    /// <param name="nickname">The nickname to insert into the database.</param>
    /// <returns>The JSON string for Python</returns>
    public string CreateUser(string first, string last, string nickname)
    {
      return this.db.CreateUser(first, last, nickname);
    }

    /// <summary>
    /// Modifies an existing user
    /// </summary>
    /// <param name="userId">The user id to modify</param>
    /// <param name="field">The field we wish to modify</param>
    /// <param name="value">The new value of the selected field</param>
    /// <returns>The JSON string for Python</returns>
    public string ModifyUser(int userId, string field, string value)
    {
      return this.db.ModifyUser(userId, field, value);
    }

    /// <summary>
    /// Creates a BattleLog with the specified information
    /// </summary>
    /// <param name="attacker">The attacker's id</param>
    /// <param name="defender">The defender's id</param>
    /// <param name="winner">The winner's id</param>
    /// <param name="start">The start time</param>
    /// <param name="end">The end time</param>
    /// <returns>The JSON string for Python</returns>
    public string CreateBattleLog(int attacker, int defender, int winner, DateTime start, DateTime end)
    {
      return this.db.CreateBattleLog(attacker, defender, winner, start, end);
    }

    //public string GetData(int value)
    //{
    //  return string.Format("You entered: {0}", value);
    //}

    //public CompositeType GetDataUsingDataContract(CompositeType composite)
    //{
    //  if (composite == null)
    //  {
    //    throw new ArgumentNullException("composite");
    //  }
    //  if (composite.BoolValue)
    //  {
    //    composite.StringValue += "Suffix";
    //  }
    //  return composite;
    //}
  }
}
